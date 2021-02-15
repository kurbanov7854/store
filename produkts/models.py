from django.contrib.auth.models import User
from django.db import models
from datetime import date



# Create your models here.
class Product(models.Model):
    types = (
        ('LAPTOP','LAPTOP'),
        ('PHONE','PHONE'),
        ('CAR','CAR'),
        ('PC','PC'),
    )
    #image
    #description
    # price
    name = models.CharField(max_length=80)
    image = models.ImageField(default='default.jpg')
    description = models.TextField()
    price = models.IntegerField()
    type = models.CharField(choices=types,max_length=20)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.price}"


class Order(models.Model):
    statuses = (
        ('In process', 'In process'),
        ('Delivered', 'Delivered'),
        ('Not delivered','Not Delivered')
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=28,choices=statuses, default='In products')
    date_created = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()


class Profile(models.Model):
    genders = (
        ('F','F'),
        ('F','F'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='image_suit.jpeg')
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    berth_date = models.DateField(default=date.today())
    twitter_link = models.CharField(max_length=100)

