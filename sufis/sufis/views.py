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
            return redirect('library')
        except Exception as e:
            print(e)

    library = BookInLibrary.objects.filter(user__name='Mart Hint').all()
    on_sale_ids = Order.objects.filter(user__name='Mart Hint').values('book')
    library_on_sale = library.filter(id__in=on_sale_ids).all()
    library_not_on_sale = library.exclude(id__in=on_sale_ids).all()
    print(on_sale_ids)
    print(library_on_sale)
    print(library_not_on_sale)
    #library = BookInLibrary.objects.all()
    context = {'library_on_sale': library_on_sale,
               'library_not_on_sale': library_not_on_sale,
               'my_orders': Order.objects.filter(user__name='Mart Hint').all()}
    return render(request, 'library.html', context)

def my_orders(request):
    orders = Order.objects.filter(user__name='Mart Hint').all()
    context = {'orders': orders}    
    return render(request, 'my_orders.html', context)

