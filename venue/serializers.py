'''
Venue Serializer Module.

Docs https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
'''

from rest_framework import serializers
from .models import Venue, BusinessType
from drf_extra_fields.geo_fields import PointField

class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    business_type = BusinessTypeSerializer(read_only=True)
    location = PointField()
    class Meta:
        model = Venue
        fields = '__all__'
