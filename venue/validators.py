from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# Valid business types.
business_types = ['Community Centre', 'Public Toilet', 'Other', 'Youth Club', 'Foodbank', 'Library', 'Health Centre', 'GP']

def validate_business_type(value):
        if value and value not in business_types:
            raise ValidationError(
                _("%(value)s is not a valid business_type. Valid types are %(business_types)s"),
                params={"value": value, "business_types": business_types})
