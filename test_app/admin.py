from django.contrib import admin
from test_app.models import Department,Employee

# Register your models here.

admin.site.register(Department)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','name','department')