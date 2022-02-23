from django.urls import path
from django.contrib.auth import views as auth_views
from users.forms import LoginForm
from users import views as user_views

urlpatterns = [
    # -> Auth Views
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), {'form': LoginForm}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # -> Configuration Views
    path('profile/', user_views.profile, name='profile'),

    # -> Billing Views
]
