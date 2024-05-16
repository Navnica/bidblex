from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>/', views.product, name='product'),
    path('store/static/img/<str:filename>/', views.img, name='img'),
    path('store/static/docs/<str:filename>/', views.docs, name='docs'),
]
