from django.urls import path

from . import views

urlpatterns = [
    path('product/<slug:product_id>', views.product, name='get_product'),
    path('product/', views.product, name='product'),
    path('product-list', views.product_list, name='product_list'),


    path('product/get_free/', views.get_free_product, name='get_free_product'),


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
    path('work/product/submit', views.set_work_products, name='set_work_products'),

    path('pay-order/finish', views.finish_pay_order, name='finish_pay_order'),

    path('finish-work/', views.finish_work, name='finish_work'),
    path('work-renew/', views.work_renew, name='renew_work'),
]
