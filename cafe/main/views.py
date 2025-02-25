from django.http import HttpResponse
from django.shortcuts import render
from .models import Order, Item


def index(request):
    orders = Order.objects.all()
    items = Item.objects.all()
    data = {
        'title': 'Cafe',
        'orders': orders,
        'items': items
    }
    return render(request, 'main/index.html', data)