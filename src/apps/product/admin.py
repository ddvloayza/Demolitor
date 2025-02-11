from django.contrib import admin

from apps.product.models.product import Product, Category, ProductImage, Packaging, Flavor, Characteristic, KeyFeature, \
    FAQ

from apps.product.models.quotation_requests import QuotationRequest, QuotationRequestDetail
from django.utils.safestring import mark_safe

from apps.tag.models import SkillTag


# Inline for Flavor
class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1

class QuotationRequestDetailInline(admin.TabularInline):
    model = QuotationRequestDetail
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

# Define an inline admin descriptor for the Characteristic model
class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1  # How many empty inlines to display by default

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, CharacteristicInline, FAQInline]
    list_display = ("name", )
    search_fields = ("name",)
    filter_horizontal = ('flavors', 'packagings', 'tag', 'skill_tags', 'key_features')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "product")

@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(KeyFeature)
class KeyFeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(SkillTag)
class SkillTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ('size', 'price')
    search_fields = ('size',)

class QuotationRequestAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "contact_date",
        "generate_quotation"
    )
    inlines = [QuotationRequestDetailInline]

    @mark_safe
    def generate_quotation(self, model):
        question = "Estas segur@ de generar esta cotizacion"
        return (
                '<a href="/product/admin/generate_pdf_quotation/'
                + str(model.uuid)
                + '/" onclick="return confirm('
                + "'"
                + question
                + "'"
                + ')" >Generar Cotizacion</a>'
        )

    generate_quotation.short_description = "Convert Investment"
    generate_quotation.allow_tags = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(QuotationRequest, QuotationRequestAdmin)
