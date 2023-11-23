"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
# from core import views
from django.contrib import admin
from django.urls import  include, path  # 'include' ve 'path' modüllerini burada tek seferde ekleyin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('my_project/', admin.site.urls), #burada istenilen ad verile biler p808_admin/ yerinde
    path("", include("account_1.urls")),    
    path("", include("core.urls")),
    path("", include("about_1.urls")),
    path("", include("contact.urls")),
    # path('', views.index, name="index"),
    # path('my_name/', include('app.urls')),  # app.urls yerine kendi uygulama adınızı kullanın

]  

urlpatterns +=i18n_patterns (
    path("", include("account_1.urls")),    
    path("", include("core.urls")),
    path("", include("about_1.urls")),
    path("", include("contact.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    # path("", include("product.urls")),
)
#setttings debug true oldughu halda localda lazim olacaq
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #statik fayllarla,yeni css,javascripleri gore bilim.. 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #..hemde medialaraida mp4,mp3 de gore bilim deye
