from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from crm.choices import PAY_ORDER_STATUS_PENDING
from crm.models import Work, PayOrder


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
    work = Work.objects.filter(end_date__lt=datetime.now(), finished=False).order_by('end_date')
    pay_order = PayOrder.objects.filter(due_date__lt=datetime.now(),
                                        status=PAY_ORDER_STATUS_PENDING).order_by('due_date')
    return render(request, 'app/index.html', {'work':work, 'pay_order': pay_order})

@login_required(login_url='../login')
def customer(request):
    return render(request, 'app/../crm/templates/customer.html', {})

@login_required(login_url='../login')
def customerList(request):
    return render(request, 'app/../crm/templates/customer-list.html', {})

@login_required(login_url='../login')
def openContruction(request):
    return render(request, 'app/open-construction.html', {})  