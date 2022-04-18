from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView, ListView

from .forms import SingleGeocodeForm, BatchGeocodeForm
from .models import SingleAddressGeocode
from .utils import (
    # handle_batch_geocode_file,
    handle_user_address,
    reverse_geocode_result
)


class GeocoderHome(TemplateView):
    template_name = 'geocoder/geocoder_home.html'


@login_required()
def geocode(request):
    if request.method == 'POST':
        form = SingleGeocodeForm(request.POST)
        if form.is_valid():
            try:
                return handle_user_address(request, form)
            # When Geocoding Fails
            except:
                messages.warning(request, 'An error occurred while trying to Geocode that address. Either, the place '
                                          'does not exist or our system could not find it')
                return render(request, 'error.html')

    else:
        form = SingleGeocodeForm()

    context = {
        'form': form,
    }
    return render(request, 'geocoder/single_address_geocode.html', context)


@login_required()
def reverse_geocode(request):
    if request.method != 'POST':
        return render(request, 'geocoder/reverse_geocoding.html')
    try:
        return reverse_geocode_result(request)
    except:
        messages.warning(request, 'An error occurred while trying to Reverse-Geocode those coordinates. Either the '
                                  'coordinates are not in Lat, Lon format OR they are in some place which does not'
                                  'exist on earth. Check to see if you have not included any text in the input field')
        return render(request, 'error.html')


# TODO: Hold off on batch geocoding for now
# def batch_geocoding(request):
#     if request.method == 'POST':
#         form = BatchGeocodeForm(request.POST, request.FILES)
#         if form.is_valid():
#             return handle_batch_geocode_file(request)
#     else:
#         form = BatchGeocodeForm()
#         context = {
#             'form': form
#         }
#
#     return render(request, 'geocoder/batch_geocode.html', context)


class SingleAddressGeocodeList(ListView):
    model = SingleAddressGeocode
    context_object_name = 'single_address_geocode'
    template_name = 'geocoder/sag_list.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return SingleAddressGeocode.objects.filter(user=current_user)
