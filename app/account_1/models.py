from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Account(AbstractUser):
    username = models.CharField(_("username"), max_length=255, blank=True, null=True)
    # _("username") verbose_name-i transtlate-ə almaq üçündürki biz onu from/importdan təyin edib kodlada gettext_lazy funksiyasını yazdım
    email = models.EmailField(_("email adress"), unique=True, null=True)
    image = models.ImageField(upload_to=('accounts') , blank=True, null=True)
    # phone_number = models.CharField(max_length = 10, unique = True)

    # USERNAME_FIELD = "phone_number" #artıq admin serverə girişdə ilk olaraq email istəyəcək
    
    USERNAME_FIELD = "email" #artıq admin serverə girişdə ilk olaraq email istəyəcək
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")
