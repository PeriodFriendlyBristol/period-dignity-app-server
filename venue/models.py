from django.contrib.gis.db import models as geo_models
from django.db import models

# Create your models here.


class BusinessType(models.Model):

    label = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.label


class Venue(models.Model):

    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250, null=True, blank=True)
    show_on_website = models.BooleanField()
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250, null=True, blank=True)
    address_line_3 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=250)
    location = geo_models.PointField()

    website = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    twitter = models.CharField(max_length=250, null=True, blank=True)

    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)

    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_phone = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.CharField(max_length=100, null=True, blank=True)

    product_location = models.CharField(max_length=500)
    business_type = models.ForeignKey(BusinessType, on_delete=models.PROTECT)

    toilet = models.BooleanField(null=True)
    stock = models.BooleanField(null=True)
    wheelchair_access = models.BooleanField(null=True)

    opening_hours = models.BooleanField()
    monday_open = models.TimeField(null=True, blank=True)
    monday_close = models.TimeField(null=True, blank=True)
    tuesday_open = models.TimeField(null=True, blank=True)
    tuesday_close = models.TimeField(null=True, blank=True)
    wednesday_open = models.TimeField(null=True, blank=True)
    wednesday_close = models.TimeField(null=True, blank=True)
    thursday_open = models.TimeField(null=True, blank=True)
    thursday_close = models.TimeField(null=True, blank=True)
    friday_open = models.TimeField(null=True, blank=True)
    friday_close = models.TimeField(null=True, blank=True)
    saturday_open = models.TimeField(null=True, blank=True)
    saturday_close = models.TimeField(null=True, blank=True)
    sunday_open = models.TimeField(null=True, blank=True)
    sunday_close = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name
