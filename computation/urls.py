from django.urls import path, include
from .views import ComputationHome, IntersectionResectionHome, ComputationsDataHome, JoinDataList, PolarDataList, Cogo, CogoIntroduction
from computation import views as computation_views


urlpatterns = [
    # Computations Landing-Home Page
    path('', ComputationHome.as_view(), name='computation_home'),
    path('cogo/overview/', CogoIntroduction.as_view(), name='cogo_overview'),
    # Computation Functions
    path('join/', computation_views.join_computation, name='join_computation'),
    path('polar/', computation_views.polar_computation, name='polar_computation'),
    path('cogo/', Cogo.as_view(), name='cogo'),
    path('traverse/', computation_views.traverse, name='traverse'),
    path('leveling/', computation_views.leveling, name='leveling'),
    # Computation Data Storage
    path('table/', ComputationsDataHome.as_view(), name='computation_data_home'),
    path('table/join/', JoinDataList.as_view(), name='join_data_list'),
    path('table/polar/', PolarDataList.as_view(), name='polar_data_list'),
    # Home Views for Expanded Menus
    path('intersection-and-resection/', IntersectionResectionHome.as_view(), name='intersection_and_resection_home'),
]