from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300, default='username')
    contact = models.CharField(max_length=300, default='123456789')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Book_genre(models.Model):
    name = models.CharField(max_length=300, unique=True)

class Author(models.Model):
    name = models.CharField(max_length=300, unique=True)
    
class Books(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    published_date = models.DateField()
    genre = models.ForeignKey(Book_genre,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user_orders')
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    contact = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='contact_orders')
    order_date = models.DateTimeField(auto_now=True)
    
    
    