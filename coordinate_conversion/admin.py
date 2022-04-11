from django.contrib import admin
from .models import CoordinateTransform


@admin.register(CoordinateTransform)
class CoordinateConversionAdmin(admin.ModelAdmin):
    list_display = ('from_epsg', 'x', 'y', 'to_epsg', 'x_trans', 'y_trans', 'user')
    list_filter = ('from_epsg', 'to_epsg')
    search_fields = ('user',)
