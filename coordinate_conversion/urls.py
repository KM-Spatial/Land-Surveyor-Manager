from django.urls import path
from coordinate_conversion import views as cc_views
from .views import TransformedCoordinates

urlpatterns = [
    path('', cc_views.coordinate_transform, name='coordinate_transformation'),
    path('table/', TransformedCoordinates.as_view(), name='transformed_coordinates_list'),
]
