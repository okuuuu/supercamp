from django.shortcuts import render
from .models import Book, User, Order
from django.views import generic

class OrderView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    
    def get_queryset(self):
        return Order.objects.all()

def orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders.html', context)


def index(request):
    return render(request, 'index.html')