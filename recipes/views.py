from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredient, Step
# Create your views here.

def index(request):
    recipe_list = Recipe.objects.order_by('name')
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe.html', context)
