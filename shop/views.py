from django.shortcuts import render
from .models import Product, ProductImage
from django.http import JsonResponse
from django.forms.models import model_to_dict

def product_list(request):
    products = Product.objects.all()
  
    return render(request,'shop/products_list.html', {'products': products})
    