from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path("", views.index, name='ecommerce'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("login", views.login, name='login'),
    path("cart", views.cart, name='cart'),
]