# from contextlib import redirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from django.views import generic #generic-in içində bütün class view-ları var

from .models import Product, Category, Comment
from .forms import CommentForm, ProductItemForm


class ProductListView(generic.ListView): # Listview yəni siyahı göstərəcəyik / django başadüşəcəkki list göndərəcəyik
    template_name = 'product/list.html' # template name-i verməliyəm
    model = Product
    context_object_name = 'products' #
    paginate_by = 9 # böyükrəqəm yazsam daha maraqlı məqam ortaya çıxır   # class əsaslı view-da pagenate əlavə etməklə bitir / niyə funksiya əsaslı vieüdən class əsaslıya keçdik  sualına cavab
    #paginate listi səhifələrə bölməkdi


def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {"products": products}
    return render(request, "product/list.html", context)

def product_detail(request,product_slug ): #detail, uptdate delete deyirse o obyektin ya id -s i lazimdi yada slugi lazimdi
    product = get_object_or_404(Product, slug=product_slug)
    """product = Product.objects.get(slug=product_slug) # get - product içində olanlardan birini götürür, hansı olduğunu müəyyən etmək üçün..
    slug=product_slug / slug - Product-ın içindəki field-in adıdır, product_slug isə (request,product_slug )-ə bərabərdi, product/urls.py-ə əlavə olunmalıdı     """
    other_products = Product.objects.filter(category=product.category).exclude(
        slug=product.slug
    ).distinct() # dublicatları ləğv edir / dublicat düşən məhsulları təkə salır
    
    reviews = Comment.objects.filter(product=product).order_by('-created_at')  # məhsul field-i,product filed-i bərabər olan bizim məhsula, detail-də olan məhsula..
    #.. Comment-ləri yığ, yığ nə elə?
    review_count = reviews.count()
    product_item_form = ProductItemForm
    
    form = CommentForm()
    
    if request.method == 'POST': # eger request metod postdursa
        if 'review-form' in request.POST:
            form = CommentForm(request.POST) #request.post formdan gonderilenlerdir/onu commentforma verir
            if form.is_valid(): #eger form duzgundurse, validdirse..  
                form.instance.user = request.user #models/Comment//user beraber olsun requesti gonderene, hemin vaxti login olan kimdirse o 
                form.instance.product = product #mehsuluda bildiririk, yuxaridaki product-a beraber edirik onuda
                form.save()
                return redirect(reverse("product-detail", args=(product.slug, )))  # noqa: F821
        else:
            product_item_form = ProductItemForm(request.POST)

    context = {
        'product' : product,
        'other_products' : other_products, 
        'form' : form,
        'reviews' : reviews, # nə elə? reviews adı ilə göndər səhifəmə, sonra detail.html-də həmin revieləri     
        'review_count' : review_count,
        'form2' : product_item_form
    }
    return render(request, 'product/detail.html', context)


