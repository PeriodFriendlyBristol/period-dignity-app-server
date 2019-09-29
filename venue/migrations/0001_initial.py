# Generated by Django 2.2.5 on 2019-09-29 11:31

from django.db import migrations, models

def import_csv_data(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    venue = apps.get_model('venue', 'Venue')



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default', max_length=80)),
            ],
        ),
        migrations.RunPython(import_csv_data),
    ]
