from django.contrib import admin

from apps.tag.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)


admin.site.register(Tag, TagAdmin)
