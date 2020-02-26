from crm.choices import PAY_ORDER_STATUS_PENDING

__author__ = 'rafeg'

from .models import Employee, Position, Customer, Tools, Media, Work, Product, PayOrder
from .util import remage
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from dateutil.rrule import rrule, MONTHLY
import calendar

def set_product(product_dict):
    product_id = product_dict.get('product_id')
    num = product_dict.get('num')
    desc = product_dict.get('desc')
    price = transformeDecimal(product_dict.get('price',''))
    comp = transformeDecimal(product_dict.get('comp',''))
    alt = transformeDecimal(product_dict.get('alt',''))
    larg = transformeDecimal(product_dict.get('larg',''))
    obs = product_dict.get('obs')

    if product_id:
        product = Product.objects.filter(id=product_id)
        if product:
            product.update(num = num, desc = desc, price = price, comp = comp, alt = alt, larg = larg, obs = obs)
            product = product.get()
            return product
    product = Product.objects.create(num = num, desc = desc, price = price, comp = comp, alt = alt, larg = larg, obs = obs)
    return product        

def transformeDecimal(value):
    return value.replace('.','').replace('.','').replace(',','.')

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
    salary = float(employee_dict.get('salary').replace('.','').replace(',','.')) if employee_dict.get('salary') else None
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
    person_type = customer_dict.get('radio-person')

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
                person_type=person_type,
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
        person_type=person_type,
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
    end_date  = datetime.strptime(work_dict.get('end_date'), '%Y-%m-%d').date() if work_dict.get('end_date') else None
    start_date  = datetime.strptime(work_dict.get('start_date'), '%Y-%m-%d').date() if work_dict.get('start_date') else None
    budget = float(work_dict.get('budget').replace('.','').replace(',','.')) if work_dict.get('budget') else None
    nfe_value = float(work_dict.get('nfe_value').replace('.','').replace(',','.')) if work_dict.get('nfe_value') else None
    address = work_dict.get('address')
    address_number = work_dict.get('address_number')
    adjunct = work_dict.get('adjunct')
    cep = work_dict.get('cep')
    neighborhood = work_dict.get('neighborhood')
    city = work_dict.get('city')
    month_value = float(work_dict.get('month_value').replace('.','').replace(',','.')) if work_dict.get('month_value') else 0
    first_due_date = datetime.strptime(work_dict.get('first_due_date'), '%Y-%m-%d').date() if work_dict.get('first_due_date') else None
    customer = Customer.objects.get(id=customer_id)
    discount = float(work_dict.get('discount').replace('.','').replace(',','.')) if work_dict.get('discount') else 0

    if work_id:
        work = Work.objects.filter(id=work_id)
        if work.get().get_products_value_month() and discount <= float(work.get().get_products_value_month()):
            month_value = float(work.get().get_products_value_month()) - discount
        elif discount >= float(work.get().get_products_value_month()):
            discount = 0
            month_value = work.get().get_products_value_month()
        else:
            month_value = 0
        if work:
            old_pay_date = work.get().pay_date
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
                city=city,
                pay_date=first_due_date.day,
                first_due_date=first_due_date,
                month_value=month_value,
                discount=discount
            )
            if not work.get().finished:
                set_pay_order(work.get())
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
        city=city,
        pay_date=first_due_date.day,
        first_due_date=first_due_date,
        month_value=month_value,
        discount=0
    )
    if not work.finished:
        set_pay_order(work)
    return work

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month + 1

def set_pay_order(work):
    start_date = work.first_due_date

    month_quantity = diff_month(work.end_date, start_date)
    month_pay = list(rrule(freq=MONTHLY, count=month_quantity, dtstart=start_date.replace(day=1)))
    if len(month_pay) > 0:
        date_list = []
        if work.month_value:
            #Se o primeiro vencimento for no passado ou hoje, altera para o proximo mes
            if start_date < work.start_date:
                start_date = month_pay[0].replace(day=1).replace(month=month_pay[0].month + 1)
                month_pay = list(rrule(freq=MONTHLY, count=month_quantity, dtstart=start_date))

            for i in month_pay:
                max_day = calendar.monthrange(i.year,i.month)[1]
                value = work.month_value
                if int(max_day) < int(work.pay_date):
                    i = i.replace(day=max_day)
                else:
                    i = i.replace(day=int(work.pay_date))
                if i.date() < work.end_date:
                    if PayOrder.objects.filter(work=work, due_date__year=i.year, due_date__month=i.month).exists():
                        pay_order = PayOrder.objects.get(work=work, due_date__year=i.year,
                                                             due_date__month=i.month)
                        if pay_order.status == PAY_ORDER_STATUS_PENDING:
                            pay_order.value = value
                            pay_order.due_date = i
                            pay_order.customer = work.customer
                            pay_order.save()
                    else:
                        PayOrder.objects.update_or_create(work=work, due_date=i,
                                                          defaults={'value': value, 'customer': work.customer})

                    date_list.append(i)

        #exclui pagamentos antigos que não serão efetivados
        PayOrder.objects.filter(work=work, status=PAY_ORDER_STATUS_PENDING).exclude(due_date__in=date_list).delete()

    return work

def set_media(file, file_name):
    image = remage(file, 600)
    media = Media.objects.create(file_name=file_name, file=image)
    return media


