from django.shortcuts import render
from .models import Book, User, Order, BookInLibrary
from django.views import generic

# class ProductFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')

#     class Meta:
#         model = Order
#         fields = ['buy_sell', 'release_date'] 

def orders(request):
    q = request.GET.get('q')
    if q:
        orders = Order.objects.filter(book__book__title__icontains=q)
    else:
        orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders.html', context)

def my_library(request):
    library = BookInLibrary.objects.filter(user__name='Mart Hint').all()
    #library = BookInLibrary.objects.all()
    context = {'library': library}
    return render(request, 'library.html', context)

def my_orders(request):
    orders = Order.objects.filter(user__name='Mart Hint').all()
    context = {'orders': orders}
    return render(request, 'my_orders.html', context)

