from django.contrib import admin
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from .models import ControlNetworkPoint


@admin.register(ControlNetworkPoint)
class CNPAdmin(ImportExportModelAdmin):
    list_display = ('MonuNum', 'Type', 'Comp_sheet', 'TOPO', 'Date_Revisions',)
    list_filter = ('Type',)
    search_fields = ('MonuNum', 'Type', 'Comp_sheet', 'TOPO', 'Date_Revisions', 'Observed')