from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    protype=models.CharField(max_length=20)
    cost=models.CharField(max_length=5)
    

    def __str__(self):
        return self.name


class Customer(models.Model):
    name=models.CharField(max_length=30)
    phoneno=models.CharField(max_length=10)
    products=models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.name