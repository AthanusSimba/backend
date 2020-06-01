from django.db import models
from django.contrib.auth.models import User


class Farmer(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=120)
    birthday = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120)
    passport_id = models.CharField(max_length=120)
    county = models.CharField(max_length=120)
    sub_county = models.CharField(max_length=120)
    ward = models.CharField(max_length=120)
    farm_size = models.CharField(max_length=120)
    maize = models.BooleanField(default=False)
    beans = models.BooleanField(default=False)
    sorghum = models.BooleanField(default=False)
    daily = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    fish = models.BooleanField(default=False)
    bee = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    red_meat = models.BooleanField(default=False)

    def __str__(self):
        return self.email
