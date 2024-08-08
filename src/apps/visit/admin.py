from django.contrib import admin

from apps.visit.models.visit import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title",)




admin.site.register(Visit, VisitAdmin)
