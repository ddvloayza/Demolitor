import graphene
from django.urls import reverse


class SkillTagsType(graphene.ObjectType):
    name = graphene.String()
    color = graphene.String()


class KeyFeaturesType(graphene.ObjectType):
    name = graphene.String()


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
    price_discount = graphene.String()
    tags = graphene.String()
    rating = graphene.String()
    skill_tags = graphene.List(SkillTagsType)
    key_features = graphene.List(KeyFeaturesType)
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
    is_active = graphene.Boolean()
    url_detail = graphene.String()

    def resolve_skill_tags(self, info):
        skill_tags = []
        if self.skill_tags.all():
            return self.skill_tags.all()
        return skill_tags

    def resolve_key_features(self, info):
        key_features = []
        if self.key_features.all():
            return self.key_features.all()
        return key_features

    def resolve_url_detail(root, info):
        if root.image:
            # Obtener la request actual desde el contexto
            request = info.context

            # Usar reverse para generar la URL relativa
            relative_url = reverse('core:product_detail', args=[str(root.slug)])

            # Usar build_absolute_uri para generar la URL completa
            absolute_url = request.build_absolute_uri(relative_url)
            return absolute_url
        return ""

    def resolve_image_url(root, info):
        if root.image:
            return info.context.build_absolute_uri(root.image.url)
        return ""

