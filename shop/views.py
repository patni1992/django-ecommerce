from django.shortcuts import render
from .models import Product, ProductImage, Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict

def product_list(request, category_slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
  
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,'shop/products_list.html', {
        'products': products, 
        'categories': categories
        })

def product_item(request, id, slug):
    product = get_object_or_404(Product, pk=id)
    return render(request,'shop/product_item.html', {'product': product})

def find_state(request, id, slug):
    product = get_object_or_404(Product, pk=id)
    return render(request,'shop/product_item.html', {'product': product})
    
    