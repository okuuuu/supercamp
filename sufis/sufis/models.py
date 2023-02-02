from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    publication_date = models.DateField()
    condition = models.IntegerField()
    pages = models.IntegerField()
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=100) 
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    buy_sell = models.BooleanField()
    
# class BookInOrder(models.Model):
#     book = models.ForeignKey(Book)
#     order = models.ForeignKey(Order)

