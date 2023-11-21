from django.urls import  path  # 'include' ve 'path' modüllerini burada tek seferde ekleyin
from . import views


urlpatterns = [
    path('contact', views.contact, name="contact"),
    
]