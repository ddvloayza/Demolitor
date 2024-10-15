from django.contrib import admin

from apps.product.models.product import Product, Category, Certificate, ProductImage

from apps.product.models.quotation_requests import QuotationRequest, QuotationRequestDetail
from django.utils.safestring import mark_safe

class QuotationRequestDetailInline(admin.TabularInline):
    model = QuotationRequestDetail
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ("name", )
    search_fields = ("name",)
    prepopulated_fields = {'slug': ('name',)}


class CertificateAdmin(admin.ModelAdmin):
    list_display = ("product", "certificado" )
    search_fields = ("product__name", "lote")


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
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(QuotationRequest, QuotationRequestAdmin)
