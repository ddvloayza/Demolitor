from django.conf import settings
from django.http import Http404
from graphene_django.views import GraphQLView


class ApiGraphQLView(GraphQLView):
    def dispatch(self, request, *args, **kwargs):
        if request.user or settings.DEBUG:
            self.graphiql = True
        return super(ApiGraphQLView, self).dispatch(request, *args, **kwargs)


class PrivateApiGraphQLView(GraphQLView):
    def dispatch(self, request, *args, **kwargs):
        if (
            request.user and request.user.is_authenticated and request.user.is_staff
        ) or settings.DEBUG:
            self.graphiql = True
        else:
            if request.user and not request.user.is_staff:
                raise Http404
        return super(PrivateApiGraphQLView, self).dispatch(request, *args, **kwargs)