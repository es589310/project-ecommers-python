from celery import shared_task
# 50 000 məhsul olanda bu səhifə arxa planda işləyib sistemi axtarır,
# prosesin arxada asinxron şəkildə getməsi üçün bu proses olmalıdır

@shared_task
def update_products():
# update_products - celery ilə arxada run olacaq olandı
    products = Product.object.all()
    for product in products:
        product.filan_field = filan_shey

# bunu çağırmaq üçün, istifadə etmək üçün
"""
hər hansı bir view-a gedirik:
    -product/views.py
    -POST olan funksiyada save()-dən sonra import edib burdan ora çağırırıq
    -update_products.delay()  = delay sinxrondur, sadəcə arxada işləməyə imkan verir
    -əgər arqumentdə götürürsə o zaman listin içində verirsən, belə:
        -update_products.delay(args=[arqumentləri qeyd edirsən])

məsələn sms göndərmək lazımdı
    -yenə eyni ilə send_sms taskı yazırıq
    -əgər asinxron işləməyini istəyiriksə yəni eyni zamanda hamısına göndərməyini istəyiriksə
        -sinxron = biri bitir o biri başlayır
        -asinxron = hamısı eyni zamanda başlaya bilir
    -product/views.py asinxronda:
        -update_products.apply_async(args=[arqument varsa veririk])
        -apply isə həm arxada işlədir həmdə eyni zamanda user-lar daxil olub işini görə bilir

"""