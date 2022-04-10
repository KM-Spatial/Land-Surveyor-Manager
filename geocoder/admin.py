from django.contrib import admin
from .models import SingleAddressGeocode, ReverseGeocode


@admin.register(SingleAddressGeocode)
class SingleAddressGeocodeAdmin(admin.ModelAdmin):
    list_display = ('address', 'lat', 'lon', 'full_address')


@admin.register(ReverseGeocode)
class ReverseGeocodeAdmin(admin.ModelAdmin):
    list_display = ('lat', 'lon', 'latitude', 'longitude', 'full_address')


