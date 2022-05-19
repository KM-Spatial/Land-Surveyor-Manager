from django.urls import path
from .views import *

urlpatterns = [
    # Project Based URLs
    path('list/', ProjectList.as_view(), name='project_list'),
    path('new/', CreateProject.as_view(), name='new_project'),
    path('<slug:slug>/', ProjectDetail.as_view(), name='project_detail'),
    path('<slug:slug>/update-project/', ProjectUpdate.as_view(), name='project_update'),
    path('<slug:slug>/delete/', RemoveProject.as_view(), name='project_delete'),
    # Task Based URls
    path('task/new/', CreateTask.as_view(), name='new_task'),
]
