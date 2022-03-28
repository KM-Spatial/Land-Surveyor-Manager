from django.urls import path
from .views import ControlNetworkApp

urlpatterns = [
    path('', ControlNetworkApp.as_view(), name='control_network_app'),
]
