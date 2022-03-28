from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from users.models import Billing


class ControlNetworkApp(LoginRequiredMixin, TemplateView):
    template_name = 'control_network/index.html'

    def get_context_data(self, *args, **kwargs):
        # Retrieve the last payment detail ->
        context = super().get_context_data(*args, **kwargs)
        context['status'] = Billing.objects.filter(user=self.request.user).last()  # -> Retrieves last entry by user
        return context