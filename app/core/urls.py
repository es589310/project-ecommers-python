from . import views
from django.contrib.auth.views import LoginView

from django.urls import  path  # 'include' ve 'path' modüllerini burada tek seferde ekleyin


urlpatterns = [
    path('', views.index, name="index"),
    path('subscribe', views.subscribe, name="subscribe"),
    path('login/', LoginView.as_view(), name='login'),

    
]