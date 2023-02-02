from django.contrib import admin
from sufis.models import User, Order, Book, BookInLibrary

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Book)
admin.site.register(BookInLibrary)