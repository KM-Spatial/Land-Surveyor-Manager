from django.urls import path, include
from geocoder import views as geocoder_views
from .views import GeocoderHome, SingleAddressGeocodeList

urlpatterns = [
    path('', GeocoderHome.as_view(), name='geocoder_home'),
    # Geocoding Process
    path('single-address/', geocoder_views.geocode, name='single_address'),
    path('reverse-geocode/', geocoder_views.reverse_geocode, name='reverse_geocode'),
    # path('batch-geocode/', geocoder_views.batch_geocoding, name='batch-geocode'),

    # Geocoding Results
    path('single-address/table/', SingleAddressGeocodeList.as_view(), name='single_address_result_table'),
]