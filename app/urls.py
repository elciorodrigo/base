from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('open-construction', views.openContruction, name='employeeList'),

]