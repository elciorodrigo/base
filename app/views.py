from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def loginUser(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return index(request)
    return render(request, 'app/login.html', {})  

@login_required(login_url='../login')
def logoutUser(request):
    logout(request) 
    return loginUser(request)


@login_required(login_url='../login')
def index(request):
    return render(request, 'app/index.html', {})  

@login_required(login_url='../login')
def customer(request):
    return render(request, 'app/../crm/templates/customer.html', {})

@login_required(login_url='../login')
def customerList(request):
    return render(request, 'app/../crm/templates/customer-list.html', {})

@login_required(login_url='../login')
def openContruction(request):
    return render(request, 'app/open-construction.html', {})  