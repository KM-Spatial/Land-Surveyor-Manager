from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User

from .models import Billing, Profile
from import_export.admin import ExportActionMixin, ImportExportModelAdmin


@admin.register(Billing)
class BillingAdmin(ImportExportModelAdmin):
    list_display = ('user', 'email', 'phone', 'expire_date')
    search_fields = ('user', 'email', 'phone')
    list_filter = ('payment_method',)


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    pass


# TODO: Find a way to export user data
# class UserAdmin(ImportExportModelAdmin):
#     pass 