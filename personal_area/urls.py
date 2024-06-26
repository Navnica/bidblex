from django.urls import path
from . import views

urlpatterns = [
    path('', views.personal_area, name='personal_area'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('products', views.products, name='products'),
    path('storages', views.storages, name='storages')
]