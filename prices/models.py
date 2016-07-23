from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
