from companies.models import Company

from django.contrib import admin

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
