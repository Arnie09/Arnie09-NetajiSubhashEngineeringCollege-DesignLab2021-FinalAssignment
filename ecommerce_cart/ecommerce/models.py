from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    image = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=512, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
