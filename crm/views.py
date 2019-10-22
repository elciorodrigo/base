from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .controller import set_employee, set_customer, set_tools, set_media, set_work
from .models import Employee, Position, Customer, Tools, Media, NoteCustomer, Work, EmployeeWork
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='../login')
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

@login_required(login_url='../login')
def employee_list(request):
    employee = Employee.objects.filter(user__is_active=True)
    return render(request, 'employee-list.html', {'employee':employee})


@login_required(login_url='../login')
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
                notes = NoteCustomer.objects.filter(customer=customer)
                response['customer'] = customer
                response['notes'] = notes
            except ObjectDoesNotExist:
                return render(request, 'app/404.html', {})
        return render(request, 'customer.html', response)

@login_required(login_url='../login')
def customer_list(request):
    customer = Customer.objects.all()
    return render(request, 'customer-list.html', {'customer':customer})

@login_required(login_url='../login')
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

@login_required(login_url='../login')
def tools_list(request):
    tools = Tools.objects.all()
    return render(request, 'tools-list.html', {'tools':tools})

@login_required(login_url='../login')
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

@login_required(login_url='../login')
def set_notes(request):
    list_id = request.POST.getlist('id[]')
    list_name = request.POST.getlist('name[]')
    customer_id = request.POST.get('customer_id_note')
    for i in range(len(list_name)):
        if i < len(list_id):
            NoteCustomer.objects.filter(id=list_id[i]).update(description=list_name[i])
            print(list_id[i], list_name[i])
        else:
            nc = NoteCustomer.objects.create(customer_id=customer_id, description=list_name[i])
            list_id.append(nc.id)
            print(list_name[i])
    NoteCustomer.objects.filter(customer_id=customer_id).exclude(id__in=list_id).delete()


    print(list_id)
    print(list_name)
    redirect_url = '/customer/{}'.format(customer_id)
    return HttpResponseRedirect(redirect_url)

@login_required(login_url='../login')
def get_free_employee(request):
    employees = Employee.objects.filter().extra(where=['employee.id not in (select emp.employee_id from employee_work emp where end_date is null)']).order_by('user__first_name')
    employees_list = [{'id':employee.id, 'external_id':employee.external_id, 'name': employee.user.get_full_name()}  for employee in employees]
    response = {'employees': employees_list}
    print(response)
    return JsonResponse(response)

@login_required(login_url='../login')
def work(request, work_id=False):
    response = {}
    if request.method == 'POST':
        work = set_work(
            request.POST
        )
        redirect_url = '{}'.format(work.id)
        return HttpResponseRedirect(redirect_url)
    elif request.method == 'GET':
        if work_id:
            try:
                work = Work.objects.get(id=work_id)
                response['work'] = work
            except ObjectDoesNotExist:
                return render(request, 'app/404.html', {})
        customers = Customer.objects.all()
        employees = Employee.objects.filter().extra(where=['employee.id not in (select emp.employee_id from employee_work emp where end_date is null)']).order_by('user__first_name')
        #work_employees = EmployeeWork.objects.filter(work=work, end_date__isnull=True)
        response['customers'] = customers
        response['employees'] = employees
        #response['work_employees'] = work_employees
        print(response)
        return render(request, 'work.html', response)

@login_required(login_url='../login')
def set_work_employess(request):
    from datetime import datetime
    list_work_employees = request.POST.getlist('id[]')
    list_all_employees = request.POST.getlist('name[]')
    work_id = request.POST.get('work_id_we')
    print(list_all_employees)
    print(list_work_employees)
    for i in range(len(list_all_employees)):
        #if i < len(list_work_employees):
        #    NoteCustomer.objects.filter(id=list_id[i]).update(description=list_name[i])
        #    print(list_id[i], list_name[i])
        if i >= len(list_work_employees):
            employees_work = EmployeeWork.objects.create(employee_id=list_all_employees[i], work_id=work_id)
            list_work_employees.append(list_all_employees[i])
    EmployeeWork.objects.filter(work_id=work_id).exclude(employee_id__in=list_all_employees).update(end_date=datetime.now())
    print('-----')
    print(list_all_employees)
    print(list_work_employees)
    redirect_url = '/work/{}'.format(work_id)
    return HttpResponseRedirect(redirect_url)