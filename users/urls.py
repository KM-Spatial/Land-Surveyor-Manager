from django.urls import path
from django.contrib.auth import views as auth_views
from users.forms import LoginForm
from users import views as user_views
from .views import InvoiceList, InvoiceDetail, PaymentInfo

urlpatterns = [
    # -> Auth Views
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), {'form': LoginForm}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # -> Configuration Views
    path('profile/', user_views.profile, name='profile'),

    # -> Billing Views
    path('payment-info/', PaymentInfo.as_view(), name='payment_info'),
    path('billing/payment-form/', user_views.make_payment, name='make_payment'),
    path('billing/invoices/', InvoiceList.as_view(), name='invoice_list'),
    path('billing/invoices/<slug:slug>/', InvoiceDetail.as_view(), name='invoice_detail'),
]
