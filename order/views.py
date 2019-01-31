from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .forms import OrderForm, CustomFieldForm
from random import randint
from django.core.mail import send_mail
from cities_light.models import City
from django.contrib import messages 
from cart.cart import Cart

def order(request):
    if request.method == "POST":
        form = CustomFieldForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            cartItems = ''
            order = request.POST.copy()
            order.pop('csrfmiddlewaretoken', None)
            order['id'] = randint(0, 999999)
            
            for item in cart:
                cartItems += f"product: {item} quantity: {item.quantity}\n"
            
            order['items'] = cartItems
            subject = f"Order nr. {order['id']}"
            message = f"Dear {order['first_name']},\n\nYou have successfully placed an order.\nYour order id is {order['id']}. \n\n{cartItems}"
            send_mail(subject, message, 'admin@myshop.com', [order['email']])

            cart.clear()

            return JsonResponse({'data':order})
    else: 
        form = CustomFieldForm()
    return render(request,'order/order.html', {'form':  form})

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'order/city_dropdown.html', {'cities': cities})
    
    