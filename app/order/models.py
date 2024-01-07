from django.db import models


class Order(models.Model):
    subtotal = models.DecimalField(max_digits=16, decimal_places=2)
    total = models.DecimalField(max_digits=16, decimal_places=2)
    shipping = models.DecimalField(max_digits=16, decimal_places=2)
    user = models.ForeignKey(
        'account_1.Account',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # default=False - heçnə etməsək avtomatik False olacaq
    is_done = models.BooleanField(default=False) # yəni bu sifariş artıq çatdırılıb. Düşüb arxivə/product/model/Product Items
    # bunların arasındaki əlaqə "bir sifarişə birdən çox məhsul" 
    # ForeignKey çoxdan çoxa qoyulur, az olan və tək olana yox

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.user.email} - {self.total}"