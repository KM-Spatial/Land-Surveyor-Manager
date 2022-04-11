"""GCN_AccountManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from users.views import Dashboard
from info.views import LandingPage

# Customize Admin Interface
admin.site.site_header = 'MySurveyor Management'
admin.site.site_title = 'My-Surveyor | Digital Surveying Platform'
admin.site.index_title = 'MySurveyor Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('control-network/', include('control_network.urls')),
    path('accounts/', include('users.urls')),
    path('info/', include('info.urls')),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('geocoding/', include('geocoder.urls')),
    path('coordinate-conversation/', include('coordinate_conversion.urls')),
    path('', LandingPage.as_view(), name='landing_page'),
    # Social Auth URLs
    path('', include('social_django.urls', namespace='social'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
