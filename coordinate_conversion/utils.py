from django.contrib import messages
from django.shortcuts import render, redirect
from django.http.response import Http404
from pyproj import CRS, Transformer


# User-Input for Coordinate Transformation
def handle_coordinate_transformation(request, form):
    from_epsg = request.POST.get('from_epsg')
    y = request.POST.get('y')
    x = request.POST.get('x')
    to_epsg = request.POST.get('to_epsg')
    # Transform Coordinates
    transformer = Transformer.from_crs(int(from_epsg), int(to_epsg))
    transformed = transformer.transform(y, x)
    # Get transformation parameters
    crs_from_info = CRS.from_epsg(from_epsg)
    crs_to_info = CRS.from_epsg(to_epsg)
    from_parameter = crs_from_info.to_wkt(pretty=True)
    to_parameter = crs_to_info.to_wkt(pretty=True)
    # Save to Database?
    save_data = request.POST.get('saved')
    if save_data == 'on':
        instance = form.save(commit=False)
        # instance as defined in Model Name
        instance.x_trans = transformed[1]
        instance.y_trans = transformed[0]
        instance.user = request.user  # Save result to user profile
        instance.save()
        # form.save()
        messages.success(request, f'The transformation from {crs_from_info} to {crs_to_info} has been executed and '
                                  'stored successfully')

    context = {
        'form': form,
        'y': transformed[0],
        'x': transformed[1],
        'p_from': from_parameter,
        'p_to': to_parameter,
    }

    return render(request, 'coordinate_conversion/transformation.html', context)
