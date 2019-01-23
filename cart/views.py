from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict
from shop.models import Product
from .cart import Cart

def detail(request):
    cart = Cart()
    return render(request,'cart/detail.html', {'cart': cart})
    

def add(request):
     return JsonResponse({'data':'add'})


def remove(request):
     return JsonResponse({'data':'remove'})




    
    