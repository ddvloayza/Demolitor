import graphene
from django.urls import reverse


class ProductType(graphene.ObjectType):
    uuid = graphene.String()
    name = graphene.String()
    slug = graphene.String()
    code = graphene.String()
    description = graphene.String()
    content = graphene.String()
    image = graphene.String()
    image_url = graphene.String()
    price = graphene.String()
    tags = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
    is_active = graphene.Boolean()
    url_detail = graphene.String()

    def resolve_url_detail(root, info):
        if root.image:
            # Obtener la request actual desde el contexto
            request = info.context

            # Usar reverse para generar la URL relativa
            relative_url = reverse('core:product_detail', args=[str(root.uuid)])

            # Usar build_absolute_uri para generar la URL completa
            absolute_url = request.build_absolute_uri(relative_url)
            return absolute_url
        return ""

    def resolve_image_url(root, info):
        if root.image:
            return info.context.build_absolute_uri(root.image.url)
        return ""

