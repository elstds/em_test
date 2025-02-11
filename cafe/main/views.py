from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# TODO Обновить шаблон
def index(request):
    orders = [
        {'id': 1, 'table_number': 3, 'items': ['coffee', 'cheesecake', 'croissant'], 'total': 40, 'status': 'ready'},
        {'id': 2, 'table_number': 1, 'items': ['tea', 'burger', 'icecream'], 'total': 27, 'status': 'cooking'}
    ]
    data = {
        'title': 'Cafe',
        'orders': orders
    }
    return render(request, 'main/index.html', data)