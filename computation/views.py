from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from computation.forms import PolarForm, JoinForm
from computation.utils import calculate_polar, calculate_join
from .models import Join, Polar


class ComputationHome(TemplateView):
    template_name = 'computation/computation_home.html'


class IntersectionResectionHome(TemplateView):
    template_name = 'computation/intersection_resection_home.html'


def join_computation(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            return calculate_join(request, form)
    else:
        form = JoinForm

    context = {
        'form': form,
    }

    return render(request, 'computation/join.html', context)


def polar_computation(request):
    if request.method == 'POST':
        form = PolarForm(request.POST)
        if form.is_valid():
            return calculate_polar(request, form)
    else:
        form = PolarForm()

    context = {
        'form': form,
    }

    return render(request, 'computation/polar.html', context)


class ComputationsDataHome(TemplateView):
    template_name = 'computation/computation_data_home.html'


class JoinDataList(LoginRequiredMixin, ListView):
    model = Join
    context_object_name = 'join_data'
    template_name = 'computation/join_list.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return Join.objects.filter(user=current_user)


class PolarDataList(LoginRequiredMixin, ListView):
    model = Join
    context_object_name = 'polar_data'
    template_name = 'computation/polar_list.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return Polar.objects.filter(user=current_user)
