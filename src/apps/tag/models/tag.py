from django.db import models
from apps.core.models.base import BaseModelMixin
from apps.core.models.seo import SEOMixin
from django.utils.translation import gettext_lazy as _


class Tag(BaseModelMixin, SEOMixin):
    code = models.CharField(
        max_length=150, blank=True, verbose_name=_("Code")
    )
    
    name = models.CharField(
        max_length=150, blank=True, verbose_name=_("Title")
    )
    slug = models.SlugField(
        verbose_name=_("Slug"), max_length=128, unique=True, null=True
    )
    start_date = models.DateTimeField(auto_now_add=False, editable=True, null=True)
    end_date = models.DateTimeField(auto_now_add=False, editable=True, null=True)
    
    created_by = models.ForeignKey(
        "customuser.CustomUser",
        related_name="tag_created_by",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    company = models.ForeignKey("company.Company", on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

