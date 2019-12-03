from venue.models import Venue, BusinessType
from django.contrib.gis import admin


# Create a custom OpenStreetMaps admin page whose
# map centers over Bristol when adding a location.
class CustomOSMAdmin(admin.OSMGeoAdmin):
    default_lat = 6702086.73
    default_lon = -288083.71
    default_zoom = 14


admin.site.register(Venue, CustomOSMAdmin)
admin.site.register(BusinessType)
