from django.contrib import admin
from .models import (Category, Product, ProductItem, 
                     ProductType, Color, Size, Brand, Comment)

class InlineSizeAdmin(admin.TabularInline):
    model = Size
    extra = 1 #her artiranda 1 uste gelir,artirmaqa icaze verir
#haqqimizida punktlarini haqqimizda-nin ichine yerlesdiririk

class InlineColorAdmin(admin.TabularInline):
    model = Color
    extra = 1 

@admin.register(ProductType) 
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name'] #aboutda text yox title var
    inlines = (InlineSizeAdmin, InlineColorAdmin) #buradan InlineAboutPointAdmin birleshdirilir

admin.site.register(ProductItem)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Comment)

# admin.site.register(ProductType)

# admin.site.register(Color)
# admin.site.register(Size)