# Generated by Django 2.2.5 on 2019-09-30 13:00
from django.db import migrations
from decimal import Decimal
import datetime
import csv


def import_csv_data(apps, schema_editor):
    # We can't import the models directly as they may be a newer
    # version than this migration expects. We use the historical versions.
    Venue = apps.get_model('venue', 'Venue')
    VenueStatus = apps.get_model('venue', 'VenueStatus')
    BusinessType = apps.get_model('venue', 'BusinessType')
    SocialMedia = apps.get_model('venue', 'SocialMedia')
    Contact = apps.get_model('contact', 'Contact')

    # Build a mapping between venue status and description.
    venue_description_lookup = {
        "Pending": "Venue is pending",
        "Verified": "Venue is verified",
        "Closed:": "Venue is closed"
    }

    # Build a mapping between venue status and VenueStatus objects.
    venue_status_object_lookup = {}
    for label, description in venue_description_lookup.items():
        venue_status_object_lookup[label] = VenueStatus(label=label, description=description)
        venue_status_object_lookup[label].save()

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
        business_type_object_lookup[label] = BusinessType(label=label, description=description)
        business_type_object_lookup[label].save()

    # Dictionary to hold unique social media objects.
    social_media_lookup = {}


    def try_date_from_string(string):
        if len(string) > 0:
            return date_from_string(string)
        else:
            return None


    def date_from_string(string):
        parts = string.split(":")
        return datetime.time(int(parts[0]), int(parts[1]))


    def get_social_media_object(website, twitter, facebook):
        social_media_hash = website + twitter + facebook
        if len(social_media_hash) == 0 or social_media_hash not in social_media_lookup.keys():
            social_media = SocialMedia(website=website, twitter=twitter, facebook=facebook)
            social_media.save()
            social_media_lookup[social_media_hash] = social_media
            return social_media
        else:
            return social_media_lookup[social_media_hash]


    with open('/code/server/venue/initial_venue_data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for row in csv_reader:
            # Parse the opening times into datetime objects.
            opening_hours = row['OPENING_HOURS'] == 'True'
            if opening_hours:
                mon_open = try_date_from_string(row['MON_OPEN'])
                mon_close = try_date_from_string(row['TUE_CLOSE'])
                tue_open = try_date_from_string(row['TUE_OPEN'])
                tue_close = try_date_from_string(row['TUE_CLOSE'])
                wed_open = try_date_from_string(row['WED_OPEN'])
                wed_close = try_date_from_string(row['WED_CLOSE'])
                thu_open = try_date_from_string(row['THU_OPEN'])
                thu_close = try_date_from_string(row['THU_CLOSE'])
                fri_open = try_date_from_string(row['FRI_OPEN'])
                fri_close = try_date_from_string(row['FRI_CLOSE'])
                sat_open = try_date_from_string(row['SAT_OPEN'])
                sat_close = try_date_from_string(row['SAT_CLOSE'])
                sun_open = try_date_from_string(row['SUN_OPEN'])
                sun_close = try_date_from_string(row['SUN_CLOSE'])
            else:
                mon_open = None
                mon_close = None
                tue_open = None
                tue_close = None
                wed_open = None
                wed_close = None
                thu_open = None
                thu_close = None
                fri_open = None
                fri_close = None
                sat_open = None
                sat_close = None
                sun_open = None
                sun_close = None

            venue_status = venue_status_object_lookup[row['VENUE_STATUS']]
            business_type = business_type_object_lookup[row['BUSINESS_TYPE']]
            social_media = get_social_media_object(row['WEBSITE'], row['TWITTER'], row['FACEBOOK'])

            contact1 = Contact(phone=row['PHONE_PRIMARY'], email=row['EMAIL_PRIMARY'])
            contact1.save()
            contact2 = Contact(phone=row['PHONE_SECONDARY'], email=row['EMAIL_SECONDARY'])
            contact2.save()

            wheelchair_access = row['WHEELCHAIR_ACCESS'] == 'True'
            stock = row['STOCK'] == 'True'
            toilet = row['TOILET'] == 'True'

            venue = Venue(name=row['NAME'], description=row['DESCRIPTION'], address_line_1=row['ADDRESS1'],
                          address_line_2=row['ADDRESS2'], address_line_3=row['ADDRESS3'], city=row['CITY'],
                          postcode=row['POSTCODE'], country=row['COUNTRY'], latitude=Decimal(row['LAT']), 
                          longitude=Decimal(row['LNG']),  product_location=row['PRODUCT_LOCATION'],
                          venue_status=venue_status, business_type=business_type, toilet=toilet,
                          social_media=social_media, wheelchair_access=wheelchair_access, stock=stock,
                          opening_hours=opening_hours, monday_open=mon_open, monday_close=mon_close, 
                          tuesday_open=tue_open, tuesday_close=tue_close, wednesday_open=wed_open, 
                          wednesday_close=wed_close, thursday_open=thu_open, thursday_close=thu_close,
                          friday_open=fri_open, friday_close=fri_close, saturday_open=sat_open,
                          saturday_close=sat_close, sunday_open=sun_open, sunday_close=sun_close)
            venue.save()
            
            venue.contacts.set([contact1, contact2])
            venue.save()



class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_csv_data)
    ]
