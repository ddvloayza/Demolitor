from django.db import models
from apps.core.models.base import BaseModelMixin
from django.utils.translation import gettext_lazy as _
from tinymce_4.fields import TinyMCEModelField


class QuotationRequest(BaseModelMixin):
    client = models.CharField(_('client'), max_length=150, blank=True)
    contact_date = models.DateTimeField(blank=True, null=True)
    description = TinyMCEModelField(
        verbose_name=_('description'),
        blank=True,
        null=True
    )

    def __str__(self):
        return "{}-{}".format(self.client, self.contact_date)

    class Meta:
        verbose_name = _("QuotationRequest")
        verbose_name_plural = _("QuotationRequests")


class QuotationRequestDetail(models.Model):
    quotation_request = models.ForeignKey(QuotationRequest, related_name='quotation_request_detail', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.price_total = self.price * self.amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.amount} de {self.product.name}"

