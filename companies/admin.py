from companies.models import Company

from django.contrib import admin


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']


admin.site.register(Company, CompanyAdmin)
