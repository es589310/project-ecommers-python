from django.shortcuts import render
from order.models import Order, WishList
from product.models import ProductItem

def basket(request):
    basket = None
    if request.user.is_authenticated:
        basket = ProductItem.objects.filter(user=request.user, status=0)
    context = {
        'items': basket
    }
    return render(request, 'order/basket.html', context)

"""def basket(request):
    if request.user.is_authenticated:
        # Kullanıcı oturum açtıysa, ProductItem'ları filtrele
        items = ProductItem.objects.filter(user=request.user, status=0)
    else:
        # Kullanıcı oturum açık değilse, bir davranış belirle (örneğin, bir hata mesajı göster)
        items = None  # veya başka bir değer

    context = {'items': items}
    return render(request, 'order/basket.html', context)"""


def checkout(request):
    context = {
        'order' : Order.objects.get(user=request.user, is_done = False)
    }
    return render(request, 'order/checkout.html', context)


def wishlist(request):
    wishlist = None
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user=request.user).first()
    context = {
        'wishlist' : wishlist
    }
    return render(request, 'order/wishlist.html', context)