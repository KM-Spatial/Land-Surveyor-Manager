from django.urls import path
from .views import ControlNetworkMap, CNLanding, ControlNetworkDatabase, ControlNetworkDetail

urlpatterns = [
    path('', CNLanding.as_view(), name='control_network_landing'),  # landing-page
    path('attribute-view/', ControlNetworkDatabase.as_view(), name='control_network_attribute_view'),
    path('map-view/', ControlNetworkMap.as_view(), name='control_network_map_view'),
    path('attribute-view/<int:pk>/', ControlNetworkDetail.as_view(), name='control_network_detail'),  # -> DetailView
]
