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

    class Meta:
        db_table = 'tools'