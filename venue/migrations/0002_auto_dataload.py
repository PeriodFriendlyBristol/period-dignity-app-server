# Generated by Django 2.2.5 on 2019-09-30 13:00
import datetime


import csv
from django.db import migrations
from django.contrib.gis.geos import Point


def import_csv_data(apps, schema_editor):
    # We can't import the models directly as they may be a newer
    # version than this migration expects. We use the historical versions.
    Venue = apps.get_model('venue', 'Venue')
    BusinessType = apps.get_model('venue', 'BusinessType')

    # Build a mapping between business type and description.
    business_type_description_lookup = {
        "Community Centre": "This business is a Community Centre",
        "Health Centre": "This business is a Health Centre",
        "Youth Club": "This business is a Youth Club",
        "Library": "This business is a Library",
        "GP": "This business is a GP",
        "Public Toilet": "This business is a Public Toilet",
        "Foodbank": "This business is a Foodbank",
        "Other": "This business is undefined"
    }

    # Build a mapping between business type and BusinessType objects.
    business_type_object_lookup = {}
    for label, description in business_type_description_lookup.items():
        business_type_object_lookup[label] = BusinessType(
            label=label, description=description)
        business_type_object_lookup[label].save()

    def try_date_from_string(string):
        parts = string.split(":")
        if len(string) > 0 and len(parts) == 2:
            try:
                return datetime.time(int(parts[0]), int(parts[1]))
            except ValueError:
                print("Error parsing string: ", string, " to int")
                return None
        else:
            return None

    def timestr(string):
        if string:
            return string
        return None

    with open('/code/venue/initial_venue_data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for row in csv_reader:
            # Parse the opening times into datetime objects.
            venue = Venue.objects.create(
                name=row['NAME'],

                description=row['DESCRIPTION'],
                address_line_1=row['ADDRESS1'],
                address_line_2=row['ADDRESS2'],
                address_line_3=row['ADDRESS3'],
                city=row['CITY'],
                postcode=row['POSTCODE'],
                country=row['COUNTRY'],
                location=Point(float(row['LNG']), float(row['LAT'])),

                phone=row['PHONE_PRIMARY'],
                email=row['EMAIL_PRIMARY'],
                website=row['WEBSITE'],
                twitter=row['TWITTER'],
                facebook=row['FACEBOOK'],

                business_type=business_type_object_lookup[row['BUSINESS_TYPE']],
                toilet=row['TOILET'] == 'True',
                wheelchair_access=row['WHEELCHAIR_ACCESS'] == 'True',

                product_location=row['PRODUCT_LOCATION'],
                stock=row['STOCK'] == 'True',

                opening_hours=row['OPENING_HOURS'] == 'True',
                monday_open=timestr(row['MON_OPEN']),
                monday_close=timestr(row['MON_CLOSE']),
                tuesday_open=timestr(row['TUE_OPEN']),
                tuesday_close=timestr(row['TUE_CLOSE']),
                wednesday_open=timestr(row['WED_OPEN']),
                wednesday_close=timestr(row['WED_CLOSE']),
                thursday_open=timestr(row['THU_OPEN']),
                thursday_close=timestr(row['THU_CLOSE']),
                friday_open=timestr(row['FRI_OPEN']),
                friday_close=timestr(row['FRI_CLOSE']),
                saturday_open=timestr(row['SAT_OPEN']),
                saturday_close=timestr(row['SAT_CLOSE']),
                sunday_open=timestr(row['SUN_OPEN']),
                sunday_close=timestr(row['SUN_CLOSE']),
            )
            venue.save()


class Migration(migrations.Migration):
    dependencies = [
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_csv_data)
    ]
