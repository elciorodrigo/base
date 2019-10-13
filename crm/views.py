from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .controller import set_employee, set_customer, set_tools, set_media
from .models import Employee, Position, Customer, Tools, Media

from django.core.exceptions import ObjectDoesNotExist

def employee(request, employee_id=False):
    response = {}
    if request.method == 'POST':
        employee = set_employee(
            request.POST
        )
        redirect_url = '{}'.format(employee.id)
        return HttpResponseRedirect(redirect_url)
    elif request.method == 'GET':
        if employee_id:
            try:
                employee = Employee.objects.get(id=employee_id)
                response['employee'] = employee
            except ObjectDoesNotExist:
                return render(request, 'app/404.html', {})
        position = Position.objects.filter(active=True)
        response['position'] = position
        return render(request, 'employee.html', response)


def employee_list(request):
    employee = Employee.objects.filter(user__is_active=True)
    return render(request, 'employee-list.html', {'employee':employee})


def customer(request, customer_id=False):
    response = {}
    if request.method == 'POST':
        customer = set_customer(
            request.POST
        )
        redirect_url = '{}'.format(customer.id)
        return HttpResponseRedirect(redirect_url)
    elif request.method == 'GET':
        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
                response['customer'] = customer
            except ObjectDoesNotExist:
                return render(request, 'app/404.html', {})
        return render(request, 'customer.html', response)


def customer_list(request):
    customer = Customer.objects.all()
    return render(request, 'customer-list.html', {'customer':customer})


def tools(request, tools_id=False):
    response = {}
    if request.method == 'POST':
        tools = set_tools(
            request.POST
        )
        redirect_url = '{}'.format(tools.id)
        return HttpResponseRedirect(redirect_url)
    elif request.method == 'GET':
        if tools_id:
            try:
                tools = Tools.objects.get(id=tools_id)
                response['tools'] = tools
            except ObjectDoesNotExist:
                return render(request, 'app/404.html', {})
        return render(request, 'tools.html', response)


def tools_list(request):
    tools = Tools.objects.all()
    return render(request, 'tools-list.html', {'tools':tools})


def media(request, media_id=False):
    response = {}
    if request.POST:
        file = request.FILES.get('media_file')
        file_name = file.name.split('.')[0]
        file_name = '{}.png'.format(file_name)
        media = set_media(file, file_name)
        response = {'media':media}
        redirect_url = '{}'.format(media.id)
        return HttpResponseRedirect(redirect_url)
    else:
        if media_id:
            try:
                media = Media.objects.get(id=media_id)
                response = {'media':media}
            except ObjectDoesNotExist:
                return render(request, 'app/404.html', {})

    return render(request, 'media.html', response)