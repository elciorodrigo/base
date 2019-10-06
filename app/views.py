from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'app/index.html', {})  

def customer(request):
    return render(request, 'app/../crm/templates/customer.html', {})

def customerList(request):
    return render(request, 'app/../crm/templates/customer-list.html', {})

def openContruction(request):
    return render(request, 'app/open-construction.html', {})  