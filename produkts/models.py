from django.db import models

# Create your models here.
class Product(models.Model):







    #image
    #description
    # price
    name = models.CharField(max_length=80)
    image = models.ImageField(default='default.jpg')
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.price}"


class Order(models.Model):
    statuses = (
        ('In process', 'In process'),
        ('Delivered', 'Delivered'),
        ('Not delivered','Not Delivered')
    )
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=28,choices=statuses, default='In products')
    date_created = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()