from django.shortcuts import render
from .models import Product, ProductImage, Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict

def product_list(request, category_name=None):
    products = Product.objects.all()
    categories = Category.objects.all()
  
    if category_name:
        category = get_object_or_404(Category, name=category_name)
        products = products.filter(category=category)

    return render(request,'shop/products_list.html', {
        'products': products, 
        'categories': categories
        })


def product_item(request, id, slug):
    return render(request,'shop/product_item.html')
    
    