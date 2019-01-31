from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .forms import OrderForm, CustomFieldForm
from cities_light.models import City
from django.contrib import messages 

def order(request):
    if request.method == "POST":
        form = CustomFieldForm(request.POST)
        if form.is_valid():
            order = request.POST.copy()
            order.pop('csrfmiddlewaretoken', None)
            return JsonResponse({'data':order})
    else: 
        form = CustomFieldForm()
    return render(request,'order/order.html', {'form':  form})

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'order/city_dropdown.html', {'cities': cities})
    
    