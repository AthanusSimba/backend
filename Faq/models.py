from django.db import models


class Faqs(models.Model):
    topic = models.CharField(max_length=120)
    question = models.CharField(max_length=240)
    answer = models.TextField()

    def __str__(self):
        return self.topic
