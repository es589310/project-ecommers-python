from django.db import models
from django.utils import timezone

# Create your models here.
class ContactInfo(models.Model): #biz doldurmalıyıq, user yox
    text = models.TextField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255) 
    additional_phone_number = models.CharField( 
        max_length=255,
        null= True,
        blank=True, #çünki ola bilsinki 2-ci nömrə yoxdu null və blank qeyd olunur
        
        )
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Appealing(models.Model): #müraciət formları buradan düzəlir, bunu biz yox user doldurmalıdır
    full_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=255, null=True) 
    message = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.full_name} - {self.email}'
    
    class Meta:
        verbose_name = 'Appealing'
        verbose_name_plural = 'Appealings'
