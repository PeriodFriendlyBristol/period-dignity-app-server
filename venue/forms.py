'''
Venue Forms for validating request input
'''
from .validators import validate_business_type, validate_coordinates
from django.forms import Form, IntegerField, CharField
from django.core.validators import MinValueValidator


class GetVenueForm(Form):

    limit = IntegerField(validators=[MinValueValidator(1)])
    offset = IntegerField(validators=[MinValueValidator(1)])
    search_radius = IntegerField(validators=[MinValueValidator(1)])
    coordinates = CharField(validators=[validate_coordinates], required=False)
    business_type = CharField(validators=[validate_business_type], required=False)
