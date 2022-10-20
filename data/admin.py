# from dataclasses import fields
from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    fields = ('ename', 'eid', 'email', 'econtact')
    search_fields = ('ename', 'eid','email','econtact')

admin.site.register(Employee, EmployeeAdmin)

