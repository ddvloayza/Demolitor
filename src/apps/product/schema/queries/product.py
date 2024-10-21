import graphene

from apps.product.schema.enums.enums import ObjectiveChoices
from apps.product.schema.types.product import ProductType
from apps.product.models import Product


class ProductQuery(graphene.ObjectType):
    product_list_by_category = graphene.List(
        ProductType,
        category_uuid=graphene.String(),
        objective=ObjectiveChoices(),
        min_price=graphene.Float(),
        max_price=graphene.Float(),
        sort_by=graphene.String()  # Este argumento se utiliza para la ordenación
    )

    def resolve_product_list_by_category(self, info, category_uuid=None, objective=None, min_price=None, max_price=None, sort_by=None, **kwargs):
        print("ENTRO", objective)
        # Filtrar por categoría si se proporciona un category_uuid
        queryset = Product.objects.all()
        if category_uuid:
            queryset = queryset.filter(category_id=category_uuid)
        if objective:
            print("objective", objective)
            queryset = queryset.filter(objective=objective.value)
        # Filtrar por rango de precios si se proporciona
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        # Ordenar los productos según el parámetro sort_by
        if sort_by == "low_to_high":

            queryset = queryset.order_by("price")
            print("queryset",queryset )
        elif sort_by == "high_to_low":
            queryset = queryset.order_by("-price")
        elif sort_by == "best_selling":
            # Asume que tienes un campo que mide las ventas
            queryset = queryset.order_by("-sales")
        elif sort_by == "highest_rated":
            # Asume que tienes un campo que mide las calificaciones
            queryset = queryset.order_by("-rating")

        return queryset
