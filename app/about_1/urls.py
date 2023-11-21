from django.urls import  path  # 'include' ve 'path' modüllerini burada tek seferde ekleyin
from . import views


urlpatterns = [
    path('about_1', views.about, name="about_1"),
    
]