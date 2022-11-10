from django.contrib import admin
from django.urls import path
from ads.views import index, Cat, Ad, NewCat, NewAd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cat/', Cat.as_view()),
    path('ad/', Ad.as_view()),
    path('cat/<int:pk>/', NewCat.as_view()),
    path('ad/<int:pk>/', NewAd.as_view()),
]
