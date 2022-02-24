from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, PaymentForm
from .models import Billing
from .paynow_processing import process_valid_form


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')


# user registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created. Login now')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class PaymentInfo(LoginRequiredMixin, TemplateView):
    template_name = 'users/payment_info.html'

    def get_context_data(self, *args, **kwargs):
        # TODO: Retrieve the last payment detail ->
        context = super().get_context_data(*args, **kwargs)
        context['status'] = Billing.objects.all()[:1]
        return context


@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            process_valid_form(request, form)

    else:
        form = PaymentForm()
    return render(request, 'users/make_payment.html', context={'form': form})


class InvoiceList(LoginRequiredMixin, ListView):
    model = Billing
    template_name = 'users/invoice_list.html'
    context_object_name = 'invoice'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Billing.objects.filter(user=user).order_by('-paid_on')


class InvoiceDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Billing
    template_name = 'users/invoice_detail.html'

    def test_func(self):
        invoice = self.get_object()
        if self.request.user == invoice.user:
            return True
        return False
