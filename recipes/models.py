from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator

@python_2_unicode_compatible
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingd_text = models.TextField()

    def __str__(self):
        return self.ingd_text


@python_2_unicode_compatible
class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.IntegerField(validators=[MinValueValidator(1)])
    step_text = models.TextField()

    def __str__(self):
        # print type(self.step_number)
        # print type(str(self.step_number))
        return "Step " + str(self.step_number)
