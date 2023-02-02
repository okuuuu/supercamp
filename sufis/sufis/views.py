from django.shortcuts import render
from .models import Book, User, Order


def index(request):
    return render(request, 'index.html')