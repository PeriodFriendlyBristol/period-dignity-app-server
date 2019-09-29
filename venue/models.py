from django.db import models

# Create your models here.


class BusinessType(models.Model):

    label = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class VenueStatus(models.Model):

    label = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class SocialMedia(models.Model):

    website = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)


class Venue(models.Model):

    name = models.CharField(max_length=80, default='Default')
    description = models.CharField(max_length=250)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250)
    address_line_3 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=250)

    product_location = models.CharField(max_length=500)
    business_type = models.ForeignKey(BusinessType, on_delete=models.PROTECT)
    venue_status = models.ForeignKey(VenueStatus, on_delete=models.PROTECT)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.PROTECT)

    toilet = models.BooleanField()
    stock = models.BooleanField()
    wheelchair_access = models.BooleanField()

    opening_hours = models.BooleanField()
    monday_open = models.TimeField()
    monday_close = models.TimeField()
    tuesday_open = models.TimeField()
    tuesday_close = models.TimeField()
    wednesday_open = models.TimeField()
    wednesday_close = models.TimeField()
    thursday_open = models.TimeField()
    thursday_close = models.TimeField()
    friday_open = models.TimeField()
    friday_close = models.TimeField()
    saturday_open = models.TimeField()
    saturday_close = models.TimeField()
    sunday_open = models.TimeField()
    sunday_close = models.TimeField()
