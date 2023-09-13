from django.contrib import admin
from .models import Company, IP


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']


@admin.register(IP)
class IPAdmin(admin.ModelAdmin):
    fields = ['name', 'company', 'allow_ports']
    list_display = ['company', 'name', 'allow_ports', 'open_ports', 'status']
