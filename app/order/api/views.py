from rest_framework import generics
from product.api.serializers import ProductItemSerializer
from product.models import ProductItem 
from ..models import Order
from .serializers import OrderIsDoneSerializer, OrderSerializer
from rest_framework.response import Response
import json 

class ProductItemDeleteAPIView(generics.DestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    lookup_field = 'id' 


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        
        
        data = serializer.data
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

        return Response({"detail": "OK", 'data': data}, status=201)
    

class OrderIsDoneAPIView(generics.UpdateAPIView): 
    queryset = Order.objects.all() 
    serializer_class = OrderIsDoneSerializer
    lookup_field = 'id' 

    def put(self, request, *args, **kwargs): 
        order_id = self.kwargs.get('id', None)  
        order = Order.objects.get(id=order_id) 
        order.is_done = True 
        order_items = ProductItem.objects.filter(order=order) 
        order_items.update(status=2) 
        print('order_items', order_items)
        return super().put(request, *args, **kwargs)
    



"""
from rest_framework import generics
from product.api.serializers import ProductItemSerializer
from product.models import ProductItem # hansı modeldən söhbət gedir onu bildirir
from ..models import Order
from .serializers import OrderIsDoneSerializer, OrderSerializer
from rest_framework.response import Response
import json 

# bu API ilə Remove funksiyasını aktiv etdik, x-i basanda səbətdən silsin
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
    


class OrderIsDoneAPIView(generics.UpdateAPIView): # UpdateAPIView = hansı fieald-lar göndərilə bilər, nələr dəyişdirilə bilər bunların nəzarəti olmasa front tərəfdən APİ-ya müdaxilə ola bilər, ancaq is_done üçün seilizer yazdıq   
    # ayrıca seializer yazmaqda məqsədimiz təhlükəsizliyi qorumaqdır, məqsədlər üçün serializer yazmaq doğrudu, ancaq əlçatanlığı qorumaq üçün, məsələn silmək üçün ayrıca serializer yazmaq üçündə yazın
    queryset = Order.objects.all() # 
    serializer_class = OrderIsDoneSerializer
    lookup_field = 'id' # generics-dən import edib updateapiviev-lə bu api classı törətdik/(axtarılacaq field)

    def put(self, request, *args, **kwargs): # UpdateAPIView olduğu üçün biz put metodunu tətbiq edirik
        #  *args tipi tuple, **kwargs tipi dict/istənilən sayda funksiya götürə bilir
        order_id = self.kwargs.get('id', None) # dict-dən açar sözü ya get ya da [] ilə götürürük/ 
        order = Order.objects.get(id=order_id) # və o id-nin qarşılığını götürüb order_id dəyərinə bərabər edirik/
        order.is_done = True # sonra isə ordero-in tamamlanmasını doğrula(order içində is_done varmı yoxla)/
        order_items = ProductItem.objects.filter(order=order) # order-i bizim order olan itemlari tap, onun statuslarını tap və o 0(BASKET)-dır onu 2(DONE) et/
        order_items.update(status=2) # onun statuslarını tap, ORDER_STATUS-a bax və default 0(BASKET)-dır onu 2(DONE) et .update metodu ile/
        print('order_items', order_items)
        return super().put(request, *args, **kwargs)"""