from . import views
from django.urls import  path  # 'include' ve 'path' modüllerini burada tek seferde ekleyin



urlpatterns = [
    path('basket', views.basket, name='basket'),
    path('checkout', views.checkout, name='checkout'),
    path('wishlist', views.wishlist, name='wishlist'),


]