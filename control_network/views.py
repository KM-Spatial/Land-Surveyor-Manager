from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from users.models import Billing
from .models import ControlNetworkPoint


class CNLanding(LoginRequiredMixin, TemplateView):
    template_name = 'control_network/control_network_landing.html'


class ControlNetworkDatabase(LoginRequiredMixin, ListView):
    model = ControlNetworkPoint
    template_name = 'control_network/control_network_database.html'
    context_object_name = 'control_point'

    # def get_queryset(self):
    #     query = self.request.GET.get('control_point')
    #     control_search = ControlNetworkPoint.objects.filter(
    #         Q(MonuNm__icontains=query) | Q(MonuNum__contains=query) | Q(Comp_sheet__contains=query) |
    #         Q(TOPO__contains=query))
    #     return control_search


class ControlNetworkMap(LoginRequiredMixin, TemplateView):
    template_name = 'control_network/control_network_map.html'

    def get_context_data(self, *args, **kwargs):
        # Retrieve the last payment detail ->
        context = super().get_context_data(*args, **kwargs)
        context['status'] = Billing.objects.filter(user=self.request.user).last()  # -> Retrieves last entry by user
        return context


class ControlNetworkDetail(LoginRequiredMixin, DetailView):
    model = ControlNetworkPoint
    template_name = 'control_network/control_network_detail.html'

    def get_context_data(self, *args, **kwargs):
        # Retrieve the last payment detail ->
        context = super().get_context_data(*args, **kwargs)
        context['status'] = Billing.objects.filter(user=self.request.user).last()  # -> Retrieves last entry by user
        return context
