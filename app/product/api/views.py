from rest_framework import generics
from rest_framework.response import Response

from ..models import ProductItem
from .serializers import ProductItemSerializer


class ProductItemCreateAPIView(generics.CreateAPIView): # yaratmaq views-u CreateAPIView-dir
   
    queryset = ProductItem.objects.all() # hansı modelin instance-lərini yaradacyıqsa onu yazırıq - ProductItem
    serializer_class = ProductItemSerializer # serializer-ə ehtiyac duyur, həmən faylın içinədə bax

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        # data=request.data - API ilə göndərilən sorğunun datası
        # serializer = self.serializer_class(data=request.data, context={"request": request})
        # context={"request": request} - əgər serializer.py-də user requesti göndərsəydik buna lazım olacaqdı
        serializer.is_valid(raise_exception=True) # formun içindəki sorğu düzgündürsə, növbəti sətrə keçsin / yox əgər düzgün data göndərilməyibsə raise ilə error qaldırsın (if şərtinin sinonimi)
        instance = serializer.save() # save oldusa, yeni bir product_item yarandı, serialzerin save olunmuş halıdıır
        instance.user = request.user # user serializers.py-də user qeyd etmədiyimiz üçün burde ayrıca request edirik 
        instance.save() # və birdə save edirik, dəyişikliklər yadda qalır
        

        data = serializer.data # bu kod sətri göndərdiyimiz APİ sorğusunu aydın görə bilməyimiz üçündür, DEPLOY-da istifadə olunmur

        return Response(data={"detail": "OK", 'data': data}, status=201)
    
     # class ProductItemCreateAPIView(generics.aşağıda
        """
        .GenericAPIView(ümumidir, hamısını birdən götürür)
        .ListCreateAPİView(listi görmək və yaratmaq üçündür)
        .RetrieveAPIView(get, yəni əldə etmək, görmək üçündür) 
        .RetrieveDestroyAPIView(həm görmək, həmdə silmək üçündür) / 
            -GET method, requiest göndərsək nəyi görmək İstəsəm həmən obyekti qaytaracaq   
            -DELETE method və ya requiesti göndərsəm, obyekti silib onun İD-ni qaytaracaq
            -PUT göndərə bilmərik
        .RetrieveUpdateDestroyAPIView()
            - GET methodunu görmək üçün = Retrieve
            - PUT methodunu update etmək üçün = Update
            - DELETE methodunu silmək üçün = Destroy   
        """