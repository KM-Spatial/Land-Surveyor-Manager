from django.contrib import admin
from .models import FAQ, Notification


@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'description')
    search_fields = ('question',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('posted_on', 'priority_level', 'title', 'message')
    list_filter = ('priority_level',)
    search_fields = ('title', 'message')

