from django.contrib import admin
from .models import Join, Polar


@admin.register(Join)
class JoinAdmin(admin.ModelAdmin):
    list_display = ('start_name', 'y_start', 'x_start', 'end_name', 'y_end', 'x_end')
    search_fields = ('user',)


@admin.register(Polar)
class PolarAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'x', 'y', 'distance', 'direction')
    search_fields = ('user',)
