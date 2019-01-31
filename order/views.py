from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .forms import OrderForm, CustomFieldForm

def order(request):
    if request.method == "POST":
        return JsonResponse({'order':'23423423'})
    
    form = CustomFieldForm()
    return render(request,'order/order.html', {'form':  form})
    
    