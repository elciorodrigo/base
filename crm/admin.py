from django.contrib import admin
from .models import Employee, Position, Customer, Tools


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

