from django.contrib import admin

from .models import Recipe, Ingredient, Step

# Register your models here.

# class RecipeAdmin(admin.ModelAdmin):
#     fields = ['']

admin.site.register(Recipe)
