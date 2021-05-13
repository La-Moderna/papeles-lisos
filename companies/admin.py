from companies.models import Company

from django.contrib import admin

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']


admin.site.register(Company, CompanyAdmin)
