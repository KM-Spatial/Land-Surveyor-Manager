from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .forms import CoordinateForm
from .models import CoordinateTransform
from .utils import handle_coordinate_transformation


@login_required
def coordinate_transform(request):
    if request.method == 'POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            return handle_coordinate_transformation(request, form)
    else:
        form = CoordinateForm()

    context = {
        'form': form,
    }

    return render(request, 'coordinate_conversion/transformation.html', context)


class TransformedCoordinates(LoginRequiredMixin, ListView):
    model = CoordinateTransform
    context_object_name = 'transformed_coordinates'
    template_name = 'coordinate_conversion/transformed_coordinates_list.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return CoordinateTransform.objects.filter(user=current_user)
