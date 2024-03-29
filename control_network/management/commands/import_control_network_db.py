class Command(BaseCommand):
    help = 'Import CSV data into the Django model'
    app_label = 'control_network'

    def handle(self, *args, **options):
        import csv
        from control_network.models import ControlNetworkPoint

        with open('https://raw.githubusercontent.com/KM-Spatial/Land-Surveyor-Manager/master/control_network/control_network_db.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                obj = ControlNetworkPoint()
                obj.MonuNum = row['MonuNum']
                obj.Run_no = row['Run_no']
                obj.MonuNm = row['MonuNm']
                obj.Type = row['Type']
                obj.Comp_sheet = row['Comp_sheet']
                obj.TOPO = row['TOPO']
                obj.Gauss_Lo = row['Gauss_Lo']
                obj.LO = row['LO']
                obj.Y_Gauss = row['Y_Gauss']
                obj.Y_LO = row['Y_LO']
                obj.X_Gauss = row['X_Gauss']
                obj.X_LO = row['X_LO']
                obj.MSL_Hgt = row['MSL_Hgt']
                obj.H_acc = row['H_acc']
                obj.LatCD = row['LatCD']
                obj.LonCD = row['LonCD']
                obj.P_acc = row['P_acc']
                obj.CM_UTM = row['CM_UTM']
                obj.UTMCM = row['UTMCM']
                obj.E_UTM = row['E_UTM']
                obj.Y_UTM = row['Y_UTM']
                obj.N_UTM = row['N_UTM']
                obj.X_UTM = row['X_UTM']
                obj.Lat_WGS84 = row['Lat_WGS84']
                obj.Lon_WGS84 = row['Lon_WGS84']
                obj.P84_acc = row['P84_acc']
                obj.EllpHgt = row['EllpHgt']
                obj.H84_acc = row['H84_acc']
                obj.Geoid_Sep = row['Geoid_Sep']
                obj.Src_Geoid = row['Src_Geoid']
                obj.PedHgt = row['PedHgt']
                obj.PillHgt = row['PillHgt']
                obj.TopSignal = row['TopSignal']
                obj.BotSignal = row['BotSignal']
                obj.Establ = row['Establ']
                obj.Date_Revisions = row['Date_Revisions']
                obj.Observed = row['Observed']
                obj.Computed = row['Computed']
                obj.Last_insp = row['Last_insp']
                obj.Destroy = row['Destroy']
                obj.DegSqr = row['DegSqr']
                obj.Invest = row['Invest']
                obj.Check = row['Check']
                obj.Remark = row['Remark']
                obj.Intervisibility = row['Intervisibility']
                obj.AREA_NM = row['AREA_NM']
                obj.Township = row['Township']
                obj.Reported_by = row['Reported_by']
                obj.save()
