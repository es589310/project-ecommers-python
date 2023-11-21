from django.shortcuts import render
from .models import About
# Create your views here.

def about(request):
    about = About.objects.first()
    context = {
        'about' : about
    }
    return render(request, "about_1/index.html", context)
    # return render(request, "about_1/about.html")