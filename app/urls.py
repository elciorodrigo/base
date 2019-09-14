from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee', views.employee, name='employee'),
    path('employee-list', views.employeeList, name='employeeList'),
    path('customer', views.customer, name='employee'),
    path('customer-list', views.customerList, name='employeeList'),
    path('open-construction', views.openContruction, name='employeeList'),

]