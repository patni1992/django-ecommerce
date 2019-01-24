from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.views.decorators.http import require_http_methods
from shop.models import Product
from .cart import Cart


def detail(request):
    cart = Cart(request)
    
    return render(request,'cart/detail.html', {'cart': cart})

@require_http_methods(["POST"])
def add(request, product_id):
     product = get_object_or_404(Product, pk=product_id)
     cart = Cart(request)
     cart.add(product)

     return redirect('shop:product_item', id=product.id, slug=product.slug)

@require_http_methods(["POST"])
def update(request):
    cart = Cart(request)

    for item in cart:
        cart.update(item, request.POST[str(item.id)])

    return redirect('cart:detail')


def remove(request):
     return JsonResponse({'data':'remove'})




    
    