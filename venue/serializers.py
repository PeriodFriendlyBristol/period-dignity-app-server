from rest_framework import serializers

from .models import Venue, SocialMedia, VenueStatus, BusinessType


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class VenueStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueStatus
        fields = '__all__'


class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
