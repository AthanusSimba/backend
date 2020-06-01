from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_general = models.BooleanField(default=True)
    is_scientist = models.BooleanField(default=False)
    is_government = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
