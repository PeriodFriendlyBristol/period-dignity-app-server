'''
Venue Forms for validating request input
'''
from django.forms import Form, IntegerField, CharField
from django.core.validators import MinValueValidator
from .validators import validate_business_type


class GetVenueForm(Form):

    limit = IntegerField(validators=[MinValueValidator(1)])
    offset = IntegerField(validators=[MinValueValidator(1)])
    business_type = CharField(validators=[validate_business_type])
