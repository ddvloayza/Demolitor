from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer
from reportlab.lib import colors
from django.http import HttpResponse
from django.conf import settings
import os
from apps.product.models import QuotationRequest


def admin_generate_pdf_quotation(request, quotation_uuid):

    quotation = QuotationRequest.objects.get(uuid=quotation_uuid)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="cotizacion_{quotation.client}.pdf"'

    # Crear un objeto PDF con ReportLab
    buffer = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    static_path = settings.STATIC_ROOT
    image_path = os.path.join(static_path, 'img/logo.jpg')  # Reemplaza con el nombre de tu imagen

    # Dibujar la imagen en el PDF
    img = Image(image_path, width=100, height=50)  # Ajusta el tamaño según sea necesario
    img.hAlign = 'LEFT'
    elements.append(img)
    elements.append(Spacer(1, 40))
    # Datos de la tabla
    data = [
        ["Encabezado 1", "Encabezado 2", "Encabezado 3"],
        ["Fila 1, Columna 1", "Fila 1, Columna 2", "Fila 1, Columna 3"],
        ["Fila 2, Columna 1", "Fila 2, Columna 2", "Fila 2, Columna 3"],
        # Más filas según sea necesario...
    ]

    # Crear la tabla
    table = Table(data)

    # Estilos opcionales para la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    table.setStyle(style)

    # Añadir la tabla a los elementos del documento
    elements.append(table)

    # Construir el PDF
    buffer.build(elements)
    return response
