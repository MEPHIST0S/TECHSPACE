from django.contrib import admin
from .models import Employee, Department, Position

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    fields = [field.name for field in Employee._meta.fields]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]
    fields = [field.name for field in Department._meta.fields]

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Position._meta.fields]
    fields = [field.name for field in Position._meta.fields]