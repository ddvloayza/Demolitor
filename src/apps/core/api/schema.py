import graphene
from django.conf import settings

from apps.product.schema.queries.product import ProductQuery


class DemolitorQueries(ProductQuery, graphene.ObjectType):
    product_queries = graphene.Field(ProductQuery)

    def resolve_product_queries(self, info, **kwargs):
        return ProductQuery()


class DemolitorMutation(graphene.ObjectType):
    pass


if settings.DEBUG:
    demolitor_scheme = graphene.Schema(query=DemolitorQueries)
else:
    demolitor_scheme = graphene.Schema(query=DemolitorQueries)