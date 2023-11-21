from django.contrib import admin
from .models import ContactInfo, Appealing

admin.site.register(ContactInfo) #biz doldurmalıyıq
admin.site.register(Appealing) #müraciət formları buradan düzəlir, bunu biz yox user doldurmalıdır