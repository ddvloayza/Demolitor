from django.contrib import admin

from apps.contact.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name",)


admin.site.register(Contact, ContactAdmin)