from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect


def order(request):
     return render(request,'order/order.html')
    
    