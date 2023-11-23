from django.db import models
# from ..utils.models import BaseModel # utils/models.py-deki basdemodel-dan goturur

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class Category(BaseModel):
    name = models.CharField(max_length=255)
    child = models.ManyToManyField(
        'self',
        # on_delete=models.CASCADE, #bu foreginkey olarsa istifade olacaqdi
        # related_name=''
        # null=True, # manytomany olduqu uchun
        blank=True
    )

    slug = models.SlugField(
        unique=True,
        null=True, #ama default deyer olmadiqi uchun lazimdi
        blank=True, #ama default deyer olmadiqi uchun lazimdi
    )

    is_parent = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'