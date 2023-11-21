from django.contrib import admin
from .models import About, AboutPoint
# Register your models here.

class InlineAboutPointAdmin(admin.TabularInline):
    model = AboutPoint
    extra = 1 #her artiranda 1 uste gelir,artirmaqa icaze verir
#haqqimizida punktlarini haqqimizda-nin ichine yerlesdiririk

@admin.register(About) 
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title'] #aboutda text yox title var
    inlines = (InlineAboutPointAdmin,) #buradan InlineAboutPointAdmin birleshdirilir

# admin.site.register(AboutPoint)  