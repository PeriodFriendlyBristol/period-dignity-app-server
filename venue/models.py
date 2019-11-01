from django.db import models

# Create your models here.


class BusinessType(models.Model):

    label = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.label


class Venue(models.Model):

    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250, null=True)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250, null=True)
    address_line_3 = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    website = models.CharField(max_length=250, null=True)
    facebook = models.CharField(max_length=250, null=True)
    twitter = models.CharField(max_length=250, null=True)

    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=250)

    product_location = models.CharField(max_length=500)
    business_type = models.ForeignKey(BusinessType, on_delete=models.PROTECT)

    toilet = models.BooleanField(null=True)
    stock = models.BooleanField(null=True)
    wheelchair_access = models.BooleanField(null=True)

    opening_hours = models.BooleanField()
    monday_open = models.TimeField(null=True)
    monday_close = models.TimeField(null=True)
    tuesday_open = models.TimeField(null=True)
    tuesday_close = models.TimeField(null=True)
    wednesday_open = models.TimeField(null=True)
    wednesday_close = models.TimeField(null=True)
    thursday_open = models.TimeField(null=True)
    thursday_close = models.TimeField(null=True)
    friday_open = models.TimeField(null=True)
    friday_close = models.TimeField(null=True)
    saturday_open = models.TimeField(null=True)
    saturday_close = models.TimeField(null=True)
    sunday_open = models.TimeField(null=True)
    sunday_close = models.TimeField(null=True)

    def __str__(self):
        return self.name
