from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from users.models import Billing


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.PasswordInput(attrs={'class': 'form-control'})


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class PaymentForm(ModelForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
    }))
    phone = forms.CharField(required=True, label='Mobile Number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'phone',
    }))
    amount = forms.CharField(required=False, label='Amount Due (ZWL)', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'id': 'price',
        'readonly': True,
        'value': 1  # -> Change this when going live
    }))

    class Meta:
        model = Billing
        fields = ('email', 'phone', 'amount', 'payment_method')

