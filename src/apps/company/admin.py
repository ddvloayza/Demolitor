from django.contrib import admin

from apps.company.models.company import Company

from apps.contact.models import CompanyM2MContact


class CompanyM2MContactInline(admin.TabularInline):  # or admin.StackedInline
    model = CompanyM2MContact  # This points to the intermediary table for the many-to-many relationship
    extra = 1  # Number of empty forms to display

class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyM2MContactInline]
    list_display = ("comercial_name", "social_reason")
    search_fields = ("comercial_name",)


admin.site.register(Company, CompanyAdmin)
