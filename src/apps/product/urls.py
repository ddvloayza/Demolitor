from django.urls import path

from apps.product.views.admin import admin_generate_pdf_quotation

urlpatterns = [
    path(
        "admin/generate_pdf_quotation/<uuid:quotation_uuid>/",
        admin_generate_pdf_quotation,
        name="generate_pdf_quotation",
    ),
]
