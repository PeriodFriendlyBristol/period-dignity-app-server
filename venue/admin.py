from django.contrib import admin
from .models import Venue, SocialMedia, VenueStatus, BusinessType

admin.site.register(Venue)
admin.site.register(SocialMedia)
admin.site.register(VenueStatus)
admin.site.register(BusinessType)
