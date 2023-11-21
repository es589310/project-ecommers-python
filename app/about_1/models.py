from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_1')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Haqqimizda"  
        verbose_name_plural = "Haqqimizda"

class AboutPoint(models.Model):
    about = models.ForeignKey(
        'about_1.About',  #1. hansi modelin ichindedise onu veririk/app-in adi sonra modelin adi
        on_delete= models.CASCADE , #about silinerse deye CASCADE
        related_name= 'points',
    )
    text = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = "Haqqimizda punktu"  
        verbose_name_plural = "Haqqimizda punktalari"