from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# Valid business types.
business_types = ['Community Centre', 'Public Toilet', 'Other', 'Youth Club', 'Foodbank', 'Library', 'Health Centre', 'GP']

def validate_business_type(value):
    # Check this is a business type that we know.
    if value not in business_types:
        raise ValidationError(
            _("Ensure this parameter is in %(business_types)s"),
            params={"business_types": business_types})

def validate_coordinates(value):
    # Ensure there are two values.
    if len(value.split(",")) != 2:
        raise ValidationError(
            _("Ensure this parameter is a comma-separated latitude & longitude string, e.g. coordinates=51.4545,-2.5879"))

    # Ensure they're floating point numbers.
    for val in value.split(","):
        try:
            float(val)
        except ValueError:
            raise ValidationError("Ensure latitude & longitude are floating point numbers")
