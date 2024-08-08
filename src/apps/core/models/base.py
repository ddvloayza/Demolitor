import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models


class BaseModelMixin(models.Model):
    """ """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    updated_at = models.DateTimeField(editable=False, auto_now=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
