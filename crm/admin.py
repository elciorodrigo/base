from django.contrib import admin
from .models import Employee, Position, Customer, Tools, Media, NoteCustomer, EmployeeWork, Work, Product, PayOrder, \
    ProductWork


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user']
    search_fields = ('user', )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ('user', )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'corporate_name']
    search_fields = ('corporate_name', )


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ('name', )


@admin.register(Media)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_name']
    search_fields = ('file_name', )


@admin.register(NoteCustomer)
class NoteCustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer']
    search_fields = ('id', 'description' )


@admin.register(EmployeeWork)
class EmployeeWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'work']
    search_fields = ('id', )


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'description']
    search_fields = ('id', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'num', 'desc']
    search_fields = ('id', )


@admin.register(PayOrder)
class PayOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'work', 'customer', 'due_date', 'value', 'work']
    search_fields = ('id', )


@admin.register(ProductWork)
class ProductWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'work', 'product']
    search_fields = ('id', )
