from django.db import models
from django.contrib.staticfiles import finders


class ContactData(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    contact_data = models.ForeignKey(ContactData, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class ProductDoc(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='docs')
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='store/static/docs')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='store/static/img/')
