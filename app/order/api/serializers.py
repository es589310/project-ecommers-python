from rest_framework import serializers

from order.views import WishList
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Order
        exclude = ('is_done',)


class OrderIsDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('is_done',)


class AddToWishListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WishList
        fields = ('product',)

"""
from rest_framework import serializers
from ..models import Order


#bu serial. order yaranması üçün/məhsul yaransın, məhsulu götürsün sifarişə, sifarişi calasın request göndərən user-a
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Order
        exclude = ('is_done',)

#bu serial. modeli yuxardaki ilə eynidir,
#burdaisə order-i update edəndə yekunlaşdı tamamlandı kimi is_done edirik         
class OrderIsDoneSerializer(serializers.ModelSerializer):
    # əlavə serializer yazmaq səbəsimiz
    class Meta:
        model = Order
        fields = ('is_done',)
"""