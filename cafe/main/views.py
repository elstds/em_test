from django.http import HttpResponse
from django.shortcuts import render
from .models import Order


def index(request):
    orders = Order.objects.all()
    data = {
        'title': 'Cafe',
        'orders': orders
    }
    return render(request, 'main/index.html', data)