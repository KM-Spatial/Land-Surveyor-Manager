from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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
    

class Traverse(models.Model):
    traverse_name = models.CharField(max_length=250)
    start_latitude = models.FloatField()
    start_longitude = models.FloatField()
    distance = models.TextField()
    angle = models.TextField()
    end_lat = models.FloatField()
    end_lon = models.FloatField()
    
    class Meta:
        verbose_name_plural = 'Traversing'
        
    def __str__(self):
        return self.traverse_name
    
"""
Leveling Calculator Models 
calculate reduced levels using the Rise and Fall method 
"""

class LevelingProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    initial_rl = models.DecimalField(max_digits=10, decimal_places=3)
    final_rl = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return f"{self.project_name} - {self.date_created.date()}"

class LevelingReading(models.Model):
    project = models.ForeignKey(LevelingProject, on_delete=models.CASCADE, related_name='readings')
    station = models.CharField(max_length=50)
    bs = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    is_sight = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    fs = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    rise = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    fall = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    rl = models.DecimalField(max_digits=10, decimal_places=3)
    remarks = models.CharField(max_length=200, blank=True)
    reading_order = models.IntegerField()

    class Meta:
        ordering = ['reading_order']
    
    
