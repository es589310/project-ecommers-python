from django.db import models
from order.models import WishList
from utils.current_request import get_current_request
# from ..utils.models import BaseModel # utils/models.py-deki basdemodel-dan goturur

ORDER_STATUSES = ( # tuple ichinde tuple-dan ibaretdir  
    (0, 'BASKET'), #
    (1, 'CHECKOUT'),
    (2, 'DONE'),
)

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
    image = models.ImageField(
        upload_to='categories',
        null=True,
        blank=True,
    )
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Brand(BaseModel): #bura məhsul tipidi: Ayaqqabı
    name = models.CharField(max_length=255)
    logo = models.FileField(
        upload_to='brands',
        null=True,
        blank=True        
        )
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

class ProductType(BaseModel): #bura məhsul tipidi: Ayaqqabı
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Product type'
        verbose_name_plural = 'Product types'

class Size(BaseModel):
    product_type = models.ForeignKey(
        ProductType,
        related_name='sizes',
        on_delete=models.PROTECT,
        null=True
    )
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'    

class Color(BaseModel):
    product_type = models.ForeignKey(
        ProductType,
        related_name='colors',
        on_delete=models.PROTECT,
        null=True

    )
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors' 

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=16, #max_digits=rəqəmlərin sayı(milyon yazılsa deyə)
        decimal_places=2, #decimal_places=qiymətlərdəki vergüldən sonrarki rəqəm sayı
        null=True, #sonradan əlavə null true etmək lazımdı
        ) 
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT, #Category silindiyi halda məhsul silinməsin
        related_name='products',
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='products',
        null=True
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
        related_name='products'
    )
    image = models.ImageField(
        upload_to="products",
        null=True, # qalan şəkil yerlərinin boş saxlaya bilməsi üçün, error verməməsi üçün null true mütləqdir

    )
    
    slug = models.SlugField(
        unique=True,
        null=True, #ama default deyer olmadiqi uchun lazimdi
        blank=True, #ama default deyer olmadiqi uchun lazimdi
    )
    has_discount = models.BooleanField(default=False)
    old_price = models.DecimalField(
        'əvvəlki qiymət',
        decimal_places=2,
        max_digits=10,
        null=True,
        blank=True
    )
    adding_to_basket_count = models.PositiveIntegerField(
        default = 0
    )

    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_price = self.price

    def save(self):
        if self.cache_price and self.cache_price != self.price:
            self.has_discount = self.cache_price > self.price
            self.old_price = self.cache_price
        return super().save()
    

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @property
    def has_added_to_wish_list(self):
        request = get_current_request()
        wl = WishList.objects.filter(user=request.user).first()
        product = Product.objects.filter(id=self.id).first()
        return bool(wl and product and product in wl.product.all())

# class ProductImage(models.Model):
#     product = models.ForeignKey(
#         Product, # əgər bağlıycağım kode bu yazılan modeldən yuxarıdadırsa dırnaqsız yazılır 
#         on_delete=models.CASCADE,
#         related_name='images'
#     )
#     image = models.ImageField(upload_to='products')

class ProductItem(BaseModel):
    user = models.ForeignKey( # bu user ile orderitem ilə əlaqəni yaratdıq
        'account_1.Account',
        related_name='order_items',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, # Məhsul silindiyi halda item-lar silinsin
        related_name='items'
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.PROTECT,
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(
        'order.Order', # əgər bağlıycağım model bu yazılan modeldən aşağıdadırsa dırnaqla, appinadı.Modelinadı olaraq yazılır
        on_delete=models.SET_NULL,
        related_name='items',
        null=True,
        blank=True,
    )
    status = models.IntegerField(
        choices=ORDER_STATUSES,
        default=0 #BASKET birinci gelmelidir
    )

    def __str__(self) -> str:
        return self.product.name
    
    @property
    def get_total_price(self):
        return self.quantity * self.product.price
    
    class Meta:
        verbose_name = 'Product item'
        verbose_name_plural = 'Products items'
        default_related_name = 'product_items'

class Comment(BaseModel): # created_at, updated_at götürməsi lazımdı
    user = models.ForeignKey(
        'account_1.Account',
        on_delete=models.CASCADE,
        
        
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        
    )
    text = models.TextField()

    def __str__(self) -> str:
        return self.user.email
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        default_related_name='comments'