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
    manufacturer = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class ProductDoc(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='docs')
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='store/static/docs')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='store/static/img/')


class Storage(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class ProductStorage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='storages')
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='products')
    count = models.IntegerField(default=0)
