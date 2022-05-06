from django.db import models


class ControlNetworkPoint(models.Model):
    MonuNum = models.CharField(max_length=50, blank=True, null=True)
    Run_no = models.CharField(max_length=50, blank=True, null=True)
    MonuNm = models.CharField(max_length=50, blank=True, null=True)
    Type = models.CharField(max_length=50, blank=True, null=True)
    Comp_sheet = models.CharField(max_length=50, blank=True, null=True)
    TOPO = models.CharField(max_length=50, blank=True, null=True)
    Gauss_Lo = models.CharField(max_length=50, blank=True, null=True)
    LO = models.CharField(max_length=50, blank=True, null=True)
    Y_Gauss = models.CharField(max_length=50, blank=True, null=True)
    Y_LO = models.CharField(max_length=50, blank=True, null=True)
    X_Gauss = models.CharField(max_length=50, blank=True, null=True)
    X_LO = models.CharField(max_length=50, blank=True, null=True)
    MSL_Hgt = models.CharField(max_length=50, blank=True, null=True)
    H_acc = models.CharField(max_length=50, blank=True, null=True)
    LatCD = models.CharField(max_length=50, blank=True, null=True)
    LonCD = models.CharField(max_length=50, blank=True, null=True)
    P_acc = models.CharField(max_length=50, blank=True, null=True)
    CM_UTM = models.CharField(max_length=50, blank=True, null=True)
    UTMCM = models.CharField(max_length=50, blank=True, null=True)
    E_UTM = models.CharField(max_length=50, blank=True, null=True)
    Y_UTM = models.CharField(max_length=50, blank=True, null=True)
    N_UTM = models.CharField(max_length=50, blank=True, null=True)
    X_UTM = models.CharField(max_length=50, blank=True, null=True)
    Lat_WGS84 = models.CharField(max_length=50, blank=True, null=True)
    Lon_WGS84 = models.CharField(max_length=50, blank=True, null=True)
    P84_acc = models.CharField(max_length=50, blank=True, null=True)
    EllpHgt = models.CharField(max_length=50, blank=True, null=True)
    H84_acc = models.CharField(max_length=50, blank=True, null=True)
    Geoid_Sep = models.CharField(max_length=50, blank=True, null=True)
    Src_Geoid = models.CharField(max_length=50, blank=True, null=True)
    PedHgt = models.CharField(max_length=50, blank=True, null=True)
    PillHgt = models.CharField(max_length=50, blank=True, null=True)
    TopSignal = models.CharField(max_length=50, blank=True, null=True)
    BotSignal = models.CharField(max_length=50, blank=True, null=True)
    Establ = models.CharField(max_length=50, blank=True, null=True)
    Date_Revisions = models.CharField(max_length=50, blank=True, null=True)
    Observed = models.CharField(max_length=50, blank=True, null=True)
    Computed = models.CharField(max_length=50, blank=True, null=True)
    Last_insp = models.CharField(max_length=50, blank=True, null=True)
    Destroy = models.CharField(max_length=50, blank=True, null=True)
    DegSqr = models.CharField(max_length=50, blank=True, null=True)
    Invest = models.CharField(max_length=50, blank=True, null=True)
    Check = models.CharField(max_length=50, blank=True, null=True)
    Remark = models.CharField(max_length=50, blank=True, null=True)
    Intervisibility = models.CharField(max_length=50, blank=True, null=True)
    AREA_NM = models.CharField(max_length=50, blank=True, null=True)
    Township = models.CharField(max_length=50, blank=True, null=True)
    Reported_by = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.MonuNm

    class Meta:
        verbose_name_plural = 'Geodetic Control Network'











