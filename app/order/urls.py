from . import views
from django.urls import  path  # 'include' ve 'path' modüllerini burada tek seferde ekleyin



urlpatterns = [
    path('basket', views.basket, name='basket'),
]