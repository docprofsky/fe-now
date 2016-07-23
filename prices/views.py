from django.shortcuts import render
from .models import Item
# Create your views here.

def index(request):
    item_list = Item.objects.order_by('name')
    print item_list
    context = {'item_list': item_list}
    return render(request, 'prices/prices.html', context)
