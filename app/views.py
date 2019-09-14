from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'app/index.html', {})  

def employee(request):
    return render(request, 'app/employee.html', {})  

def employeeList(request):
    return render(request, 'app/employee-list.html', {})  

def customer(request):
    return render(request, 'app/customer.html', {})  

def customerList(request):
    return render(request, 'app/customer-list.html', {})  