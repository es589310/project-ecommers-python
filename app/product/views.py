from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category
from django.views import generic #generic-in içində bütün class view-ları var



class ProductListView(generic.ListView): # Listview yəni siyahı göstərəcəyik / django başadüşəcəkki list göndərəcəyik
    template_name = 'product/list.html' # template name-i verməliyəm
    model = Product
    context_object_name = 'products' #
    paginate_by = 2 # böyükrəqəm yazsam daha maraqlı məqam ortaya çıxır   # class əsaslı view-da pagenate əlavə etməklə bitir / niyə funksiya əsaslı vieüdən class əsaslıya keçdik  sualına cavab
    #paginate listi səhifələrə bölməkdi

def products_by_category(requset, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'products' : products
    }
    return render(requset, 'product/list.html', context)

def product_detail(request,product_slug ): #detail, uptdate delete deyirse o obyektin ya id -s i lazimdi yada slugi lazimdi
    product = get_object_or_404(Product, slug=product_slug)
    product = Product.objects.get(slug=product_slug)
