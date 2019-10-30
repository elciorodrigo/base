from django.urls import path

from . import views

urlpatterns = [
    path('product/<slug:product_id>', views.product, name='get_product'),
    path('product/', views.product, name='product'),
    path('product-list', views.product_list, name='product_list'),


    # path('employee/get_free/', views.get_free_employee, name='get_free_employee'),


    path('customer/<slug:customer_id>', views.customer, name='get_customer'),
    path('customer/', views.customer, name='customer'),
    path('customer-list', views.customer_list, name='customer_list'),
    #path('customer/notes/submit', views.set_notes, name='set_notes'),

    # path('tools/<slug:tools_id>', views.tools, name='get_tools'),
    # path('tools/', views.tools, name='tools'),
    # path('tools-list', views.tools_list, name='tools_list'),

    # path('media/<slug:media_id>', views.media, name='get_tools'),
    # path('media/', views.media, name='media'),

    path('work/', views.work, name='work'),
    path('work/<slug:work_id>', views.work, name='get_work'),
    path('work-list', views.work_list, name='work_list'),
    path('work/employees/submit', views.set_work_employees, name='set_work_employess'),
]