'''
Venue Serializer Module.

Docs https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
'''

from rest_framework import serializers
from .models import Venue, BusinessType
from django.contrib.gis.geos import Point

class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        
    def to_representation(self, obj):
        return {
            "latitude": obj[1],
            "longitude": obj[0]
        }


class VenueSerializer(serializers.ModelSerializer):
    business_type = BusinessTypeSerializer(read_only=True)
    location = PointSerializer(read_only=True)
    class Meta:
        model = Venue
        fields = '__all__'
