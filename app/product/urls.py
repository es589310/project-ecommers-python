from . import views
from django.urls import  path  # 'include' ve 'path' modüllerini burada tek seferde ekleyin



urlpatterns = [
    path('products', views.ProductListView.as_view(), name='products'),
    path('products/categories/<slug:category_slug>', views.products_by_category, name='products-by-category'),
    path('products/<slug:product_slug>', views.product_detail, name='product-detail'),
    path('search', views.search, name='search'),

]