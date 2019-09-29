from django.db import models

# Create your models here.


class Venue(models.Model):

    name = models.CharField(max_length=80, default='Default')

