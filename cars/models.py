from django.db import models


class Cars(models.Model):
    model = models.CharField(max_length=150)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
