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
    isbn = models.CharField(max_length=512)
    pages = models.IntegerField()
    language = models.CharField(max_length=512)
    genre = models.CharField(max_length=512)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self) -> str:
        return self.name
    
class BookInLibrary(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture_link = models.CharField(max_length=512)
    is_public = models.BooleanField()
    status = models.CharField(max_length=512)
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookInLibrary, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    buy_sell = models.BooleanField()
    def __str__(self):
        return f'{str(self.user)} - {str(self.book.book)}'

    
# class BookInOrder(models.Model):
#     book = models.ForeignKey(Book)
#     order = models.ForeignKey(Order)

