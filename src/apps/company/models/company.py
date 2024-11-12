from django.db import models
from apps.core.models.base import BaseModelMixin
from apps.core.models.seo import SEOMixin
from apps.company.utils import custom_company_upload_to
from django.utils.translation import gettext_lazy as _
from apps.company import constants
from ubigeos.models import Distrito, Provincia, Region


class Company(BaseModelMixin, SEOMixin):
    social_reason = models.CharField(
        max_length=150, blank=True, verbose_name=_("Razon Social")
    )
    comercial_name = models.CharField(
        max_length=150, blank=True, verbose_name=_("Comercial Name")
    )
    type_company = models.CharField(
        verbose_name=_("Genero"),
        choices=constants.TYPE_COMPANY_CHOICES,
        max_length=60,
        blank=True,
        null=True,
    )
    comercial_activity = models.CharField(
        max_length=150, blank=True, verbose_name=_("Comercial Activity")
    )
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, blank=True, null=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(
        verbose_name=_("image_logo_company"),
        upload_to=custom_company_upload_to,
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=150, blank=True, verbose_name=_("Address")
    )
    email = models.CharField(
        max_length=150, blank=True, verbose_name=_("Email")
    )
    phone_number = models.CharField(
        max_length=150, blank=True, verbose_name=_("phone_number")
    )
    contacts = models.ManyToManyField('contact.CompanyM2MContact', related_name='company_contacts', blank=True, null=True,)
    facebook_url = models.URLField(null=True, blank=True, verbose_name=_("Facebook URL"))
    instagram_url = models.URLField(null=True, blank=True, verbose_name=_("Instagram URL"))
    tiktok_url = models.URLField(null=True, blank=True, verbose_name=_("TikTok URL"))
    whatsapp_url = models.URLField(null=True, blank=True, verbose_name=_("Whatsapp URL"))

    def __str__(self):
        return "{}".format(self.comercial_name)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")


