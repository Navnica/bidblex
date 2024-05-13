from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>/', views.product, name='product'),
    path('product/<int:pk>/store/static/img/<str:filename>', views.img, name='img'),
    path('login/', views.login, name='login')
]
