from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SingleAddressGeocode(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    full_address = models.TextField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    html_map = models.TextField(null=True, blank=True)
    # Save to user account 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Meta-Data (might be useful someday)
    meta_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Single-Address'


class ReverseGeocode(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    full_address = models.TextField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    html_map = models.TextField(null=True, blank=True)
    # Save to user account 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Meta-Data (might be useful someday)
    meta_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_address

    class Meta:
        verbose_name_plural = 'Reverse'
