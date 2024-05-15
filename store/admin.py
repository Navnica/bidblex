from django.contrib import admin
from .models import ContactData, Product, ProductImage, ProductDoc

admin.site.register(ContactData)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductDoc)