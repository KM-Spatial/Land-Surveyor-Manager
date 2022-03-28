from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from info.models import FAQ


class LandingPage(TemplateView):
    template_name = 'info/landing_page.html'


class FaQ(ListView):
    model = FAQ
    template_name = 'info/faq.html'
    context_object_name = 'faq'


def faq(request):
    return render(request, 'info/faq.html')


def pricing(request):
    return render(request, 'info/pricing.html')


def terms_conditions(request):
    return render(request, 'info/terms_and_conditions.html')


def privacy_policy(request):
    return render(request, 'info/privacy_policy.html')


def contact_us(request):
    return render(request, 'info/contact.html')
