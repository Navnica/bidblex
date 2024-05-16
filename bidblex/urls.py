from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('store.urls')),
    path('personal_area/', include('personal_area.urls')),
]
