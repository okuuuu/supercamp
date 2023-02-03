from django.shortcuts import render, redirect
from .models import Book, User, Order, BookInLibrary
from django.views import generic
from django import forms
from .models import Order
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
    if request.method == 'POST':
        print(request.POST)
        try:
            price = float(request.POST['price'])
            book_id = int(request.POST['book_in_library'])
            book = BookInLibrary.objects.get(pk=book_id)
            user = User.objects.filter(name='Mart Hint').all()[0]
            order = Order.objects.create(price=price, book=book, user=user, buy_sell=True)
            order.save()
        except Exception as e:
            print(e)
    q = request.GET.get('q')
    if q:
        library = BookInLibrary.objects.filter(book__title__icontains=q).filter(user__name='Mart Hint')
    else:
        library = BookInLibrary.objects.filter(user__name='Mart Hint').all()
    #library = BookInLibrary.objects.all()
    context = {'library': library}
    return render(request, 'library.html', context)

def my_orders(request):
    q = request.GET.get('q')
    if q:
        orders = Order.objects.filter(book__book__title__icontains=q).filter(user__name='Mart Hint')
    else:
        orders = Order.objects.filter(user__name='Mart Hint').all()
    context = {'orders': orders}
    return render(request, 'my_orders.html', context)

