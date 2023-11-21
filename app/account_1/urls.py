from django.urls import path
# from .views import AccountRegistrationView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register', views.AccountRegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = "account_1/login.html"), name = 'Login' ),
    #settings.py-də LOGIN_REDIRECT_URL = '/' daxil etmək lazımdır
    path('logout/', auth_views.LogoutView.as_view(template_name = "home/index.html"), name = 'Logout' ),
    ]
#as_view() classı çevirir funksiyaya