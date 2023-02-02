from django.shortcuts import render
from .models import Book, User, Order
from django.views import generic
import django_filters

# class ProductFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')

#     class Meta:
#         model = Order
#         fields = ['buy_sell', 'release_date'] 

def orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders.html', context)


def index(request):
    return render(request, 'index.html')