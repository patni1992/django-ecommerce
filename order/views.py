from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .forms import OrderForm, CustomFieldForm
from random import randint
from django.core.mail import send_mail
from cities_light.models import City
from django.contrib import messages 
from .models import OrderItem
from cart.cart import Cart

def order(request):
    if request.method == "POST":
        form = CustomFieldForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            order = form.save()
            
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item,
                                         price=item.price,
                                         quantity=item.quantity)

            mail = order.create_mail(cart)
            send_mail(**mail)
            cart.clear()

            return render(request,
                          'order/receipt.html',
                          {'order': order})
    else: 
        form = CustomFieldForm()
    return render(request,'order/order.html', {'form':  form})

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'order/city_dropdown.html', {'cities': cities})
    
    