from django.contrib.auth.models import User
from django.db import models

CRS = (
    ('4326', 'EPSG:4326 WGS 84'),
    ('3857', 'EPSG:3857 WGS 84 / Pseudo-Mercator'),
    ('4209', 'EPSG:4209 Arc 1950'),
    ('20935', 'EPSG: 20935 Arc 1950 / UTM zone 35S'),
    ('20936', 'EPSG: 20936  Arc 1950 / UTM zone 36S '),
    ('32735', 'EPSG: 32735 WGS 84 / UTM zone 35S'),
    ('32736', 'EPSG: 32736 WGS 84 / UTM zone 36S'),
    ('9378', 'EPSG: 9378 IGb14'),
    ('7789', 'EPSG: 7789 ITRF2014'),
    ('4979', 'EPSG: 4979 WGS 84'),
)

# Source -> https://epsg.org/search/by-name?sessionkey=zyqbsvk3e2&searchedTerms=zimbabwe


class CoordinateTransform(models.Model):
    from_epsg = models.CharField(max_length=100, choices=CRS)
    x = models.FloatField(verbose_name="X/Lon")
    y = models.FloatField(verbose_name="Y/Lat")
    to_epsg = models.CharField(max_length=100, choices=CRS)
    x_trans = models.FloatField(verbose_name='X-Transformed', null=True, blank=True)
    y_trans = models.FloatField(verbose_name='Y-Transformed', null=True, blank=True)
    stored_on = models.DateTimeField(auto_now_add=True)
    # Save to user account
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Coordinate Conversions'

    def __str__(self):
        return str(self.stored_on)
