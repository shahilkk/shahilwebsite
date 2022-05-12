from django.contrib import admin
from .models import *
# Register your models here.


# class DetailsAdmin(admin.ModelAdmin):
#     list_display = ('employee_name', 'employee_phone', 'employee_district')
#     search_fields=('employee_name',)
admin.site.register(Details)
