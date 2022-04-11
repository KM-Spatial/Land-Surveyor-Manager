from django.forms import fields, forms, ModelForm, widgets
from django import forms
from .models import CoordinateTransform


class CoordinateForm(ModelForm):
    x = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': "Longitude / X"
    }))
    y = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control mt-3 mb-3',
        'placeholder': "Latitude / Y"
    }))

    class Meta:
        model = CoordinateTransform
        fields = ('from_epsg', 'y', 'x', 'to_epsg')
