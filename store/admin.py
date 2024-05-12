from django.contrib import admin
from .models import ContactData, Product, ProductImage

admin.site.register(ContactData)
admin.site.register(Product)
admin.site.register(ProductImage)