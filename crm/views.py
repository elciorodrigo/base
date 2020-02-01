from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .controller import set_employee, set_customer, set_tools, set_media, set_work, set_product, set_pay_order
from crm.choices import PAY_ORDER_STATUS_FINISHED
from crm.models import PayOrder, ProductWork
from .models import Employee, Position, Customer, Tools, Media, NoteCustomer, Work, EmployeeWork, Product
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='../login')
def product(request, product_id=False):
    response = {}
    if request.method == 'POST':
        product = set_product(
            request.POST
        )
        redirect_url = '{}'.format(product.id)
        return HttpResponseRedirect(redirect_url)
    elif request.method == 'GET':
        if product_id:
            print('asdhafuihfdauihfdasf' + product_id)
            try:
                product = Product.objects.get(id=product_id)
                print(product)
                response['product'] = product
            except ObjectDoesNotExist:
                return render(request, 'app/404.html', {})
        return render(request, 'product.html', response)


@login_required(login_url='../login')
def product_list(request):
    product = Product.objects.all()
    return render(request, 'product-list.html', {'product':product})


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
        return render(request, 'product.html', response)

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
def get_free_product(request):
    products = Product.objects.filter().extra(where=['id not in (select prod.product_id from product_work prod where end_date is null)']).order_by('desc')
    product_list = [{'id':product.id, 'num':product.num, 'desc': product.desc}  for product in products]
    response = {'products': product_list}
    print(response)
    return JsonResponse(response)

@login_required(login_url='../login')
def work(request, work_id=False):
    response = {}
    if request.method == 'POST':
        work = set_work(
            request.POST
        )
        redirect_url = '{}?a=1'.format(work.id)
        return HttpResponseRedirect(redirect_url)
    elif request.method == 'GET':
        if work_id:
            try:
                work = Work.objects.get(id=work_id)
                product_work = ProductWork.objects.filter(work=work, end_date__isnull=True)
                response['product_work'] = product_work
                response['work'] = work
                pay_order = PayOrder.objects.filter(work=work).order_by('due_date')
                response['pay_order'] = pay_order
            except ObjectDoesNotExist:
                return render(request, 'app/404.html', {})
        customers = Customer.objects.all()
        response['customers'] = customers
        return render(request, 'work.html', response)

@login_required(login_url='../login')
def set_work_products(request):
    from datetime import datetime
    list_work_products = request.POST.getlist('id[]')
    list_all_products = request.POST.getlist('name[]')
    work_id = request.POST.get('work_id_we')
    work = Work.objects.get(id=work_id)

    product_list = []
    for i in list_all_products:
        ProductWork.objects.update_or_create(product_id=i, work_id=work_id,
                                             defaults={'start_date': work.start_date})
    ProductWork.objects.filter(work_id=work_id).exclude(product_id__in=list_all_products).update(end_date=datetime.now())
    redirect_url = '/work/{}?a=1'.format(work_id)
    return HttpResponseRedirect(redirect_url)


@login_required(login_url='../login')
def finish_pay_order(request):
    if request.method == "GET" and 'id' in request.GET:
        pay_order_id = request.GET['id']
        pay_order = PayOrder.objects.get(id=pay_order_id)
        pay_order.status = PAY_ORDER_STATUS_FINISHED
        pay_order.save()
    redirect_url = '/'
    return HttpResponseRedirect(redirect_url)


@login_required(login_url='../login')
def finish_work(request):
    if request.method == "GET" and 'id' in request.GET:
        work_id = request.GET['id']
        work_obj = Work.objects.get(id=work_id)
        work_obj.finished = True
        work_obj.save()
        ProductWork.objects.filter(work=work_obj, end_date__isnull=True).update(end_date=datetime.now())
    redirect_url = '/'
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='../login')
@csrf_exempt
def work_renew(request):
    if request.method == "POST":
        work_id = request.POST.get('work_id')
        end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
        work_obj = Work.objects.get(id=work_id)
        work_obj.end_date = end_date
        work_obj.save()
        set_pay_order(work_obj)
    return HttpResponse(json.dumps({'status':'success'}), content_type='application/json')


@login_required(login_url='../login')
def work_list(request):
    work = Work.objects.all()
    return render(request, 'work-list.html', {'works':work})