from django.db import models
from apps.core.models.base import BaseModelMixin
from apps.core.models.seo import SEOMixin
from django.utils.translation import gettext_lazy as _

from apps.company.models import Company


class Contact(BaseModelMixin):
    first_name = models.CharField(
        max_length=250, blank=True, verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=250, blank=True, verbose_name=_("Last Name")
    )
    occupation = models.CharField(
        max_length=250, blank=True, verbose_name=_("Occupation")
    )
    email = models.CharField(
        max_length=150, blank=True, verbose_name=_("Email")
    )
    phone_number = models.CharField(
        max_length=150, blank=True, verbose_name=_("Phone Number")
    )
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class CompanyM2MContact(BaseModelMixin):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} {}".format(self.company, self.contact)