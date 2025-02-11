
# Create your models here.
from django.db import models

class Item(models.Model):
    id = models.AutoField('ID', primary_key=True)  # Используем AutoField для автоматической генерации ID
    name = models.CharField('Название', max_length=100)  # Добавим max_length для поля name
    price = models.IntegerField('Цена')

class Order(models.Model):
    id = models.AutoField('ID', primary_key=True)  # Используем AutoField для автоматической генерации ID
    table_number = models.IntegerField('Номер стола')
    total_price = models.IntegerField('Общая стоимость')
    status = models.CharField('Статус', max_length=10)
    items = models.ManyToManyField(Item, related_name='orders')  # Связь многие ко многим с моделью Item