from django.contrib import admin
from employee_information.models import Department, Employees

# Register your models here.
admin.site.register(Department)
admin.site.register(Employees)
