from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.customuser.models.customuser import (
    CustomUser,
    UserProfile,
    CustomWebPage,
    Banner,
    WebPageBannerM2M,
)


class BannerCustomWebPageInline(admin.TabularInline):
    model = WebPageBannerM2M
    fk_name = "custom_web_page"
    extra = 1


class CustomUserAdmin(UserAdmin):
    """MyUser admin.
    Custom myuser admin to show data in
    admin dashboard.
    """

    list_display = ("id", "email", "is_active", "is_staff", "date_joined")
    list_filter = ("is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Role",
            {"fields": ("is_staff",)},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    # 'is_superuser',
                    # 'groups',
                    # 'user_permissions',
                )
            },
        ),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    search_fields = ("email",)

    ordering = ("-date_joined",)
    readonly_fields = ("date_joined",)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("nick_name", "user", "phone_number")
    search_fields = ("user__email",)


class CustomWebPageAdmin(admin.ModelAdmin):
    list_display = ("company_name", "email")
    inlines = (
        BannerCustomWebPageInline, 
    )

class BannerAdmin(admin.ModelAdmin):
    list_display = ("image", )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomWebPage, CustomWebPageAdmin)
admin.site.register(Banner, BannerAdmin)