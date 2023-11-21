from django.shortcuts import render
# from django.http import HttpResponse

# def index(request): #funksiya esasli view yaziriqsa mutle, ilk arqumnet request olmali 
#     return HttpResponse("Zalimin zülmü nə qədər olsada mən taab edərəm,\nEtməsin zənni-kibir zərrə yolundan çəkiləm")

def index(request): #funksiya esasli view yaziriqsa mutle, ilk arqumnet request olmali 
    return render(request, 'home/index.html') #birbaşa home,çünki djangoya html kodlarını hardan oxumağı göstərdim