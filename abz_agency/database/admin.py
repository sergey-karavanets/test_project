from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "employment_date", "salary")


admin.site.register(Employee, EmployeeAdmin)
