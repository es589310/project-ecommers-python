from django.db import models
from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=81)
    age = models.IntegerField(default=0) #
    id = models.AutoField(primary_key=True)

    def __str__(self) -> str:#serverdeli bloga authorsa yazdiqlarimizi tam gostermeyi uchun
        return self.full_name 
     
    class Meta: #serverdə class adlarını dəyişmək üçün 
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="blogs")
    note = models.TextField(null=True, blank=True) #optionalda görünməyi üçün istifadə olunur
    author = models.ForeignKey(
        Author, #blog.Author - da yaza bilerdik #foreignkey,manytomany,onetoone ilk arqumenti hans; modele baghlidirsa o yazilir
        on_delete=models.CASCADE, #əgər yazar silinərsə onun bloqlarını sil
        # # on_delete=models.PROTECT # yazarın özünü silməy olmaz, birinci bloqlarını sil sonra özünü
        # """on_delete=models.SET_NULL # author silinərsə author field-ini boş saxla/ null = True / Blank = True
        # null=True #database-də boş qalsın deməkdi
        # blank =True #yazılan formun içində boş saxlıyıb save edə bilək deyə"""

        related_name="blogs",  #tərsinə əlaqə, blogdan author-u görmək olur, ama authordan görmək olmur, buna görədə releated name tərsinə əlaqəni yaradır
        null=True,
        help_text="Bloqun yazarını seçin!",
        verbose_name="Yazar",
        )  

    
         

    def __str__(self) -> str:
        return f"{self.title[:20]}..." if len(self.title) > 10 else self.title  #bloq başlığını qısa variandtda bildirir
                #f len(self.title) > 10 = əgər self.title/başlıq, bunun uzunluğu 10-dan böyükdürsə, "{self.title[:20]}..."  = 20-a kimi kəssin
                #else self.title  = əks təqdirdə self.title özünü göstərsin
    
    class Meta:
        verbose_name = "Bloq"
        verbose_name_plural = "Bloqlar"