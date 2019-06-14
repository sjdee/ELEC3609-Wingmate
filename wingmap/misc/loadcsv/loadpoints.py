from django.contrib.gis import geos
from wingmap.models import WingmanLocation
import os

# this file is for testing purposes. Loading points with a latitude and longitude
# fills the databse with CSV points for testing.
# to be run from the django shell
# with:
#   execfile('wingmap/misc/loadcsv/loadpoints.py')

point_csv = os.path.abspath(os.path.join('wingmap/misc/loadcsv', 'points.csv'))

def load_points():
    with open(point_csv) as point_file:
        isHeader = True
        for line in point_file:
            if (isHeader):
                isHeader = False
                continue

            lon, lat, i, name = line.split(',')

            point = "POINT("+ lon.strip() + " " + lat.strip() + ")"
            print(point)
            r = WingmanLocation.objects.create(name=name, geom=geos.fromstr(point))

load_points()
