from django.db import models


# Create your models here.

class Feedback(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    county = models.CharField(max_length=120)
    sub_county = models.CharField(max_length=120)
    ward = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    comments = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Feedback'


from django.db import models

# Create your models here.
