from django.urls import path

from . import views

urlpatterns = [
    path('employee/<slug:employee_id>', views.employee, name='get_employee'),
    path('employee/', views.employee, name='employee'),
    path('employee-list', views.employee_list, name='employee_list'),

    path('customer/<slug:customer_id>', views.customer, name='get_customer'),
    path('customer/', views.customer, name='customer'),
    path('customer-list', views.customer_list, name='customer_list'),

    path('tools/<slug:tools_id>', views.tools, name='get_tools'),
    path('tools/', views.tools, name='tools'),
    path('tools-list', views.tools_list, name='tools_list'),
]