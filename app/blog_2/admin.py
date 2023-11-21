from django.contrib import admin
from .models import Author, Blog
# Register your models here.
# .models mütləqdir, çünki nöqtəsiz gedib ümumi moduls-a baxacaq, ama bizə blog_1 models-əbaxması lazımdı
admin.site.register(Author)
# admin.site.register(Blog)

@admin.register(Blog) #decorator ile en rahati olur
class BlogAdmin(admin.ModelAdmin):
    list_display = ['get_title','note','author']  #ichinde stringler olmalidir/ ["buraya fieldler qeyd olunur"]
    list_per_page = 50  #səhiəflərin bölünməsini təşkil edir, yoxsa admin paneldə hər şey gec aça bilər
    list_filter = ["author"] #suzgec
    # list_editable = () #hansi fieldleri edit ede bilsek onu qoyuruq
    search_fields = ['author__full_name','title'] #author__full_name deyerek oz field-ni gotururk / axtarış sistemidir,orda sehc olarsa error vermeyecek
    # save_on_top = True #yaddaşda saxlanılan yerləri yuxarı qaldırır
    # save_as = True #yenisi kimi yadda saxla
    # actions = ['']
    # add_form_template =  #template-ni override etmek uchun
    exclude = ("image",) #image field-i yoxa cixir / tuple edib sonra vergul qoymasaq error olacaq / 
    readonly_fields = ("title",) #title deyishdirilmez olaraq qalir / vergulsuz olmaz
    # prepopulated_fields = {} #title ne yazsaq onu cevirecek slug-a

    def get_title(self,obj):
        return f"{obj.title[:20]}..." if len(obj.title) > 10 else obj.title
    
    get_title.short_description = "Title"