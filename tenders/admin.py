from django.contrib import admin

# Register your models here.
from .models import Tender, Contractor, Procurer


class ProcurerInline(admin.TabularInline):
    model = Procurer
    extra = 3


class ProcurerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['company_name']}),
        (None, {'fields': ['city']}),
        (None, {'fields': ['address']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('company_name', 'city', 'address')
    # list_filter = ['city']
    search_fields = ['company_name']


admin.site.register(Procurer, ProcurerAdmin)
