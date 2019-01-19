from django.shortcuts import render
from .models import Product, ProductImage, Category
from django.http import JsonResponse
from django.forms.models import model_to_dict

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
  
    return render(request,'shop/products_list.html', {
        'products': products, 
        'categories': categories
        })
    