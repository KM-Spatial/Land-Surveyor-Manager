from django.urls import path
from info import views as info_views
from .views import FaQ

urlpatterns = [
    path('faq/', FaQ.as_view(), name='faq'),
    path('pricing/', info_views.pricing, name='pricing'),
    path('terms-and-conditions/', info_views.terms_conditions, name='terms_and_conditions'),
    path('privacy-policy/', info_views.privacy_policy, name='privacy_policy'),
    path('contact-us', info_views.contact_us, name='contact_us'),
]
