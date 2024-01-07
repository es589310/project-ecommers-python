from rest_framework import generics
from product.api.serializers import ProductItemSerializer
from product.models import ProductItem # hansı modeldən söhbət gedir onu bildirir
from ..models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
import json 

# bu API ilə Remove funksiyasını aktiv etdik
class ProductItemDeleteAPIView(generics.DestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    lookup_field = 'id' # bu API arqument kimi hansı arqument qəbul edəcək, onu bildirir(id arqumentini)


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        # instance.user = request.user
        # instance.save()

        data = serializer.data
        # data['absolute_url'] = request.build_absolute_uri(reverse("checkout"))
        Order.objects.filter(user=request.user, is_done=False).exclude(id=instance.id).delete()
        if items := json.loads(request.data.get('items', '[]')):
            for item in items: # [2, 4, 11]
                print('item', item)
                if item is not None:
                    obj = ProductItem.objects.get(
                        id=int(item),
                    )
                    obj.order = instance
                    obj.save()
                    # instance.items.add(obj) əlavə etmək üçün
                    # instance.items.remove(obj) silmək üçün

        return Response({"detail": "OK", 'data': data}, status=201)