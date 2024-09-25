import graphene

from apps.product.schema.types.product import ProductType
from apps.product.models import Product


class ProductQuery(graphene.ObjectType):

    product_list_by_category = graphene.List(
        ProductType,
        category_uuid=graphene.String()
    )

    def resolve_product_list_by_category(self, info, category_uuid=None, **kwargs):
        if category_uuid:

            return Product.objects.filter(category_id=category_uuid)
        return Product.objects.all()
