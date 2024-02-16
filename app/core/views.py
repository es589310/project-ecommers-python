from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext as _
# from django.core.mail import send_mail
from account_1.models import SubscribedUser
from product.models import Category, Product


# from django.http import HttpResponse

# def index(request): #funksiya esasli view yaziriqsa mutle, ilk arqumnet request olmali 
#     return HttpResponse("Zalimin zülmü nə qədər olsada mən taab edərəm,\nEtməsin zənni-kibir zərrə yolundan çəkiləm")

def index(request): #funksiya esasli view yaziriqsa mutle, ilk arqumnet request olmali 
    categories = Category.objects.filter(is_parent=True)
    trandy_products = Product.objects.all().order_by('-adding_to_basket_count')[:8]
    just_arrived_products = Product.objects.all().order_by('-created_at')[:8]

    context = {
        'categories' : categories,
        'trandy_products': trandy_products,
        'just_arrived_products' : just_arrived_products,
    }
    return render(request, 'home/index.html', context) #birbaşa home,çünki djangoya html kodlarını hardan oxumağı göstərdim


def subscribe(request):
    email = request.POST.get('subscribed_user')

    if request.user.is_authenticated:
        if request.user.email == email:
            if not SubscribedUser.objects.filter(email=email).first():
                SubscribedUser.objects.create(email=email)
                messages.success(request, _('Congratulations! You have subscribed succesfly!'))
                # send_mail(
                #     'Subscription',
                #     'Congratulations! You have subscribed succesfly!',
                #     'notificationtodo@gmail.com',
                #     [request.user.email]
                #     #html_message = əlavə etsək o bizə daha gözəl mesaj mətni verəcək
                #     )
                return redirect('/')
            else:
                messages.error(request, _('Oooops! You have subscribed already!'))
                return redirect('/')
        else:
            messages.error(request, _('Oooops! This email doesn`t belog to you!'))
            return redirect('/')
    else:
        messages.error(request, _('Looks like you are not logged in, please login to subscribe!'))
        return redirect('/')
    return redirect('/')
                
            