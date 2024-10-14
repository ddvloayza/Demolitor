
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ubigeos.models import Distrito, Provincia, Region

from apps.core.models.base import BaseModelMixin
from apps.core.models.seo import SEOMixin
from apps.customuser import constants
from apps.customuser.utils import custom_user_upload_to


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, name=None, **extra_fields):

        if not email:
            raise ValueError(_("El correo es un campo obligatorio."))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = None
    email = models.EmailField(
        max_length=75,
        unique=True,
    )

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)

    date_joined = models.DateTimeField(
        default=timezone.now,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class UserProfile(BaseModelMixin, SEOMixin):

    user = models.OneToOneField(
        "customuser.CustomUser",
        related_name="user_profile",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    nick_name = models.CharField(
        max_length=150, blank=True, verbose_name=_("Nick Name")
    )

    first_name = models.CharField(
        max_length=150, blank=True, null=True, verbose_name=_("First Name")
    )

    last_name = models.CharField(max_length=150, blank=True, null=True)

    type_document = models.CharField(
        verbose_name=_("Type Document"),
        choices=constants.TYPE_CHOICES,
        default=constants.TYPE_DNI,
        max_length=60,
        blank=True,
        null=True,
    )
    occupation = models.CharField(
        max_length=150, blank=True, verbose_name=_("Ocupation")
    )
    document_number = models.IntegerField(blank=True, default=0, null=True)

    gender = models.CharField(
        verbose_name=_("Genero"),
        choices=constants.GENDER_CHOICES,
        max_length=60,
        blank=True,
        null=True,
    )

    phone_number = models.IntegerField(blank=True, default=0, null=True)

    civil_status = models.CharField(
        verbose_name=_("Estado Civil"),
        choices=constants.CIVIL_CHOICES,
        max_length=60,
        blank=True,
        null=True,
    )
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null=True)
    image_profile = models.ImageField(
        verbose_name=_("image_profile"),
        upload_to=custom_user_upload_to,
        blank=True,
        null=True,
    )


    def __str__(self):
        return "{}".format(self.nick_name)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("Users Profiles")


class CustomWebPage(BaseModelMixin):
    phone_number = models.CharField(
        max_length=150, blank=True, verbose_name=_("Phone Number")
    )
    phone_number_two = models.CharField(
        max_length=150, blank=True, verbose_name=_("Phone Number Two")
    )
    email = models.CharField(
        max_length=200, blank=True, verbose_name=_("Email")
    )
    address = models.CharField(
        max_length=500, blank=True, verbose_name=_("Direccion")
    )
    company_name = models.CharField(
        max_length=150, blank=True, verbose_name=_("Company Name")
    )
    ruc = models.CharField(
        max_length=150, blank=True, verbose_name=_("RUC")
    )
    comercial_name = models.CharField(
        max_length=150, blank=True, verbose_name=_("Comercial Name")
    )
    description = models.TextField(null=True, blank=True)

    banners = models.ManyToManyField(
        "customuser.Banner",
        blank=True,
        null=True,
        related_name="banner_set",
        through="WebPageBannerM2M",
    )

    def __str__(self):
        return "{}".format(self.company_name)

    class Meta:
        verbose_name = _("CustomWebPage")
        verbose_name_plural = _("CustomWebPages")


class Banner(BaseModelMixin):
    name = models.CharField(
        max_length=500, blank=True, verbose_name=_("Nombre")
    )
    image = models.ImageField(
        verbose_name=_("image"),
        upload_to="banner",
        blank=True,
        null=True,
    )

    image_responsive = models.ImageField(
        verbose_name=_("image_responsive"),
        upload_to="banner-responsive",
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{}".format(self.name)
    
    @property
    def get_absolute_image_url(self):
        return self.image.url
    
    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")


class WebPageBannerM2M(BaseModelMixin):
    custom_web_page = models.ForeignKey("customuser.CustomWebPage", on_delete=models.CASCADE)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("WebPageBannerM2M")
        verbose_name_plural = _("WebPageBannerM2Ms ")