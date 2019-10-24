from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Position(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'name'


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=50, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    cellphone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=15, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    rg = models.CharField(max_length=10, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    address_number = models.CharField(max_length=5, blank=True, null=True)
    adjunct = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    external_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def get_format_birth_date(self):
        if self.birth_date:
            return datetime.strftime(self.birth_date, '%Y-%m-%d')
        return ''

    def get_eng_start_date(self):
        if self.start_date:
            return datetime.strftime(self.start_date, '%Y-%m-%d')
        return ''

    def get_format_start_date(self):
        if self.start_date:
            return datetime.strftime(self.start_date, '%d/%m/%Y')
        return ''

    def get_work_customer_name(self):
        employee = EmployeeWork.objects.filter(employee=self, end_date__isnull=True)
        customer = employee.get().work.customer.corporate_name if employee else ''
        return customer

    def get_work_allocated(self):
        employee = EmployeeWork.objects.filter(employee=self, end_date__isnull=True)
        work = 'Nº {} - {}'.format(employee.get().work.id, employee.get().work.customer.corporate_name) if employee else ''
        return work

    def get_work_id(self):
        employee = EmployeeWork.objects.filter(employee=self, end_date__isnull=True)
        work_id = employee.get().work.id if employee else ''
        return work_id

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        db_table = 'employee'


class Customer(models.Model):
    corporate_name = models.CharField(max_length=100)
    state_registration = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    cellphone = models.CharField(max_length=15, blank=True, null=True)
    rg = models.CharField(max_length=10, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    address_number = models.CharField(max_length=5, blank=True, null=True)
    adjunct = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.corporate_name

    class Meta:
        db_table = 'customer'


class Tools(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    voltage = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    external_id = models.IntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def get_price(self):
        price_br = "%4.2f" % self.price
        return  price_br.replace('.', ',')

    class Meta:
        db_table = 'tools'


class Media(models.Model):
    file_name = models.CharField(max_length=100)
    file = models.BinaryField()

    def __str__(self):
        return self.file_name

    def get_file(self):
        import base64
        encoded = str(base64.b64encode(self.file))
        return encoded[2:len(encoded)-1]
        #return self.file

    class Meta:
        db_table = 'media'


class NoteCustomer(models.Model):
    description = models.CharField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.id, self.customer.corporate_name)

    class Meta:
        db_table = 'note_customer'


class Work(models.Model):
    description = models.CharField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    address_number = models.CharField(max_length=5)
    adjunct = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    crated_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    nfe_value = models.FloatField(blank=True, null=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.id, self.description)

    def get_eng_start_date(self):
        if self.start_date:
            return datetime.strftime(self.start_date, '%Y-%m-%d')
        return ''

    def get_format_start_date(self):
        if self.start_date:
            return datetime.strftime(self.start_date, '%d/%m/%Y')
        return ''

    def get_eng_end_date(self):
        if self.end_date:
            return datetime.strftime(self.end_date, '%Y-%m-%d')
        return ''

    def get_format_end_date(self):
        if self.end_date:
            return datetime.strftime(self.end_date, '%d/%m/%Y')
        return ''

    class Meta:
        db_table = 'work'


class EmployeeWork(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.DO_NOTHING)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.employee.user.get_full_name(), self.work.description)

    class Meta:
        db_table = 'employee_work'