from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from shop.models import Product
from .cart import Cart

def detail(request):
    cart = Cart()
    return render(request,'cart/detail.html', {'cart': cart})
    

def add(request, product_id):
     product = get_object_or_404(Product, pk=product_id)
     cart = Cart(request)
     cart.add(product)
     return redirect('shop:product_item', id=product.id, slug=product.slug)


def remove(request):
     return JsonResponse({'data':'remove'})




    
    