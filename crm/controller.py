__author__ = 'rafeg'

from .models import Employee, Position, Customer, Tools, Media, Work
from .util import remage
from django.contrib.auth.models import User
from datetime import datetime


def set_employee(employee_dict):
    first_name = employee_dict.get('first_name')
    employee_id = employee_dict.get('employee_id')
    last_name = employee_dict.get('last_name')
    rg = employee_dict.get('rg').replace('.','').replace('-','')
    cpf = employee_dict.get('cpf').replace('.','').replace('-','')
    birth_date  = datetime.strptime(employee_dict.get('birth_date'), '%Y-%m-%d') if employee_dict.get('birth_date') else None
    start_date  = datetime.strptime(employee_dict.get('start_date'), '%Y-%m-%d') if employee_dict.get('start_date') else None
    phone = employee_dict.get('phone')
    cellphone = employee_dict.get('cellphone')
    email = employee_dict.get('email')
    address = employee_dict.get('address')
    address_number = employee_dict.get('address_number')
    adjunct = employee_dict.get('adjunct')
    cep = employee_dict.get('cep')
    neighborhood = employee_dict.get('neighborhood')
    city = employee_dict.get('city')
    position_id = employee_dict.get('position')
    salary = float(employee_dict.get('salary').replace('.','').replace(',','')) if employee_dict.get('salary') else None
    external_id = employee_dict.get('external_id')

    position = Position.objects.get(id=position_id)

    if employee_id:
        employee = Employee.objects.filter(id=employee_id)
        if employee:
            employee.update(
                rg=rg,
                cpf=cpf,
                birth_date=birth_date ,
                phone=phone,
                cellphone=cellphone,
                address=address,
                address_number=address_number,
                adjunct=adjunct,
                cep=cep,
                neighborhood=neighborhood,
                city=city,
                position=position,
                salary=salary,
                external_id=external_id,
                start_date=start_date
            )
            employee = employee.get()
            user = employee.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return employee
    username = '{}-{}'.format(external_id, first_name)
    user, _ = User.objects.get_or_create(username=username, first_name=first_name, last_name=last_name, email=email)
    try:
        employee = Employee.objects.create(
            user=user,
            rg=rg,
            cpf= cpf,
            birth_date=birth_date ,
            phone=phone,
            cellphone=cellphone,
            address=address,
            address_number=address_number,
            adjunct=adjunct,
            cep=cep,
            neighborhood=neighborhood,
            city=city,
            position=position,
            salary= salary,
            start_date=start_date,
            external_id=external_id,
        )
    except Exception as ex:
        user.delete()
        raise ex
    return employee


def set_customer(customer_dict):
    customer_id = customer_dict.get('customer_id')
    corporate_name = customer_dict.get('corporate_name')
    state_registration = customer_dict.get('state_registration')
    cnpj = customer_dict.get('cnpj')
    phone = customer_dict.get('phone')
    cellphone = customer_dict.get('cellphone')
    #email = customer_dict.get('email')
    address = customer_dict.get('address')
    address_number = customer_dict.get('address_number')
    adjunct = customer_dict.get('adjunct')
    cep = customer_dict.get('cep')
    neighborhood = customer_dict.get('neighborhood')
    city = customer_dict.get('city')

    if customer_id:
        customer = Customer.objects.filter(id=customer_id)
        if customer:
            customer.update(
                corporate_name=corporate_name,
                state_registration=state_registration,
                cnpj=cnpj,
                phone=phone,
                cellphone=cellphone,
                address=address,
                address_number=address_number,
                adjunct=adjunct,
                cep=cep,
                neighborhood=neighborhood,
                city=city,
            )
            customer = customer.get()
            return customer


    customer = Customer.objects.create(
        corporate_name=corporate_name,
        state_registration=state_registration,
        cnpj=cnpj,
        phone=phone,
        cellphone=cellphone,
        address=address,
        address_number= address_number,
        adjunct=adjunct,
        cep=cep,
        neighborhood=neighborhood,
        city=city,
    )
    return customer


def set_tools(tools_dict):
    tools_id = tools_dict.get('tools_id')
    name = tools_dict.get('name')
    voltage = tools_dict.get('voltage') if tools_dict.get('voltage') else None
    price =  float(tools_dict.get('price').replace('.','').replace(',','.')) if tools_dict.get('price') else None
    external_id = tools_dict.get('external_id') if tools_dict.get('external_id') else None
    amount = tools_dict.get('amount') if tools_dict.get('amount') else None

    if tools_id:
        tools = Tools.objects.filter(id=tools_id)
        if tools:
            tools.update(
                name=name,
                voltage=voltage,
                price=price,
                external_id=external_id,
                amount=amount
            )
            tools = tools.get()
            return tools


    tools = Tools.objects.create(
            name=name,
            voltage=voltage,
            price=price,
            external_id=external_id,
            amount=amount
    )
    return tools


def set_work(work_dict):
    description = work_dict.get('description')
    work_id = work_dict.get('work_id')
    customer_id = work_dict.get('customer')
    end_date  = datetime.strptime(work_dict.get('end_date'), '%Y-%m-%d') if work_dict.get('end_date') else None
    start_date  = datetime.strptime(work_dict.get('start_date'), '%Y-%m-%d') if work_dict.get('start_date') else None
    budget = float(work_dict.get('budget').replace('.','').replace(',','')) if work_dict.get('budget') else None
    nfe_value = float(work_dict.get('nfe_value').replace('.','').replace(',','')) if work_dict.get('nfe_value') else None
    address = work_dict.get('address')
    address_number = work_dict.get('address_number')
    adjunct = work_dict.get('adjunct')
    cep = work_dict.get('cep')
    neighborhood = work_dict.get('neighborhood')
    city = work_dict.get('city')

    customer = Customer.objects.get(id=customer_id)
    if work_id:
        work = Work.objects.filter(id=work_id)
        if work:
            work.update(
                description=description,
                customer=customer,
                start_date=start_date,
                end_date=end_date,
                budget=budget,
                nfe_value=nfe_value,
                address=address,
                address_number=address_number,
                adjunct=adjunct,
                cep=cep,
                neighborhood=neighborhood,
                city=city
            )
            return work.get()

    work = Work.objects.create(
        description=description,
        customer=customer,
        start_date=start_date,
        end_date=end_date,
        budget=budget,
        nfe_value=nfe_value,
        address=address,
        address_number=address_number,
        adjunct=adjunct,
        cep=cep,
        neighborhood=neighborhood,
        city=city
    )
    return work


def set_media(file, file_name):
    image = remage(file, 600)
    media = Media.objects.create(file_name=file_name, file=image)
    return media


