from django.contrib.auth.models import User
from django.db import models


class Join(models.Model):
    start_name = models.CharField(max_length=200, null=True, blank=True)
    y_start = models.FloatField()
    x_start = models.FloatField()
    end_name = models.CharField(max_length=200, null=True, blank=True)
    y_end = models.FloatField()
    x_end = models.FloatField()
    # Results of the Calculation to be stored
    distance = models.FloatField(null=True, blank=True)
    direction_dd = models.FloatField(null=True, blank=True)
    direction_deg = models.IntegerField(null=True, blank=True)
    direction_min = models.IntegerField(null=True, blank=True)
    direction_sec = models.FloatField(null=True, blank=True)
    # Store the date and time information too
    stored_on = models.DateTimeField(auto_now_add=True)
    # Save to user account
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Join'

    def __str__(self):
        return str(self.stored_on)


class Polar(models.Model):
    station_name = models.CharField(max_length=200, null=True, blank=True)
    x = models.FloatField()
    y = models.FloatField()
    distance = models.FloatField()
    direction = models.CharField(max_length=200)
    end_name = models.CharField(max_length=200, null=True, blank=True)
    # Results of the calculation
    x_coordinate = models.FloatField(null=True, blank=True)
    y_coordinate = models.FloatField(null=True, blank=True)
    # Store the date and time information too
    stored_on = models.DateTimeField(auto_now_add=True)
    # Save to user account
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Polar'

    def __str__(self):
        return str(self.stored_on)
