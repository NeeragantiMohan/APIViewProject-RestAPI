from django.contrib import admin
from APIViewapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','no','role','salary','location']
admin.site.register(Employee,EmployeeAdmin)