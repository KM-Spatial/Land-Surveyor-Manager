from django.urls import path, include
from .views import (
    ComputationHome, 
    IntersectionResectionHome, 
    ComputationsDataHome, 
    JoinDataList, 
    PolarDataList, 
    Cogo, 
    CogoIntroduction
)
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
    path('leveling/', computation_views.leveling, name='leveling'), # in testing phase
    path('leveling/save/', computation_views.save_leveling, name='save_leveling'), # in testing phase
    # Resection 
    path('resection/part-two/', computation_views.resection_three_points_2, name='resection_three_point_part_2'),

    # Computation Data Storage
    path('table/', ComputationsDataHome.as_view(), name='computation_data_home'),
    path('table/join/', JoinDataList.as_view(), name='join_data_list'),
    path('table/polar/', PolarDataList.as_view(), name='polar_data_list'),
    path('table/leveling/<int:project_id>/', computation_views.load_leveling, name='load_leveling'), # in testing phase
    # Home Views for Expanded Menus
    path('intersection-and-resection/', IntersectionResectionHome.as_view(), name='intersection_and_resection_home'),
]