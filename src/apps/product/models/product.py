from django.db import models
from apps.core.models.base import BaseModelMixin
from apps.core.models.seo import SEOMixin
from apps.product.utils import custom_category_upload_to, custom_product_upload_to
from django.utils.translation import gettext_lazy as _
from tinymce_4.fields import TinyMCEModelField
from slugify import slugify
from django.urls import reverse
from django.contrib.sites.models import Site

class Category(BaseModelMixin, SEOMixin):
    name = models.CharField(
        max_length=150, blank=True, verbose_name=_("Name")
    )
    slug = models.SlugField(
        verbose_name=_("Slug"), max_length=128, unique=True, null=True
    )
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, null=True, blank=True, related_name="category_company")
    image = models.ImageField(
        verbose_name=_("image_category"),
        upload_to=custom_category_upload_to,
        blank=True,
        null=True,
    )
    description = TinyMCEModelField(null=True, blank=True)
    content = TinyMCEModelField(
        verbose_name=_('Content'),
        blank=True,
        null=True
    )
    
    @property
    def get_absolute_image_url(self):
        return self.image.url
    
    @property
    def get_products(self):
        return Product.objects.filter(category=self)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            slug = slug.replace("-", "")
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                slug_exits = Category.objects.filter(slug=slug).exists()
                if slug_exits:
                    slug = self.slug + str(counter)
                    counter += 1
                else:
                    self.slug = slug
                    break
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")



class Product(BaseModelMixin, SEOMixin):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    code = models.CharField(
        max_length=150, blank=True, verbose_name=_("Code")
    )

    name = models.CharField(
        max_length=150, blank=True, verbose_name=_("Name")
    )
    slug = models.SlugField(
        verbose_name=_("Slug"), max_length=128, unique=True, null=True
    )
    description = TinyMCEModelField(null=True, blank=True)
    content = TinyMCEModelField(
        verbose_name=_('Content'),
        blank=True,
        null=True
    )

    image = models.ImageField(
        verbose_name=_("image_principal_product"),
        upload_to=custom_product_upload_to,
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00,
        verbose_name="price",
    )

    tag = models.ManyToManyField("tag.Tag", verbose_name=_("Tags"), blank=True, related_name="product_tags")
    
    @property
    def get_absolute_image_url(self):
        if self.image:
            return self.image.url
        else:
            return ""
    
    @property
    def get_absolute_url_product(self):
        current_site = Site.objects.get_current()
        return f"https://{current_site.domain}{reverse('core:product_detail', args=[str(self.uuid)])}"
    
    @property
    def get_latest_products(self):
        return Product.objects.all().order_by("created_at")[:3]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            slug = slug.replace("-", "")
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                slug_exits = Product.objects.filter(slug=slug).exists()
                if slug_exits:
                    slug = self.slug + str(counter)
                    counter += 1
                else:
                    self.slug = slug
                    break
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(
        verbose_name=_("Product Image"),
        upload_to=custom_product_upload_to,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return "{}-{}".format(self.product.name, self.lote)


class Certificate(BaseModelMixin, SEOMixin):

    certificado = models.FileField(
        verbose_name=_("certificado"),
        upload_to='certificados/',
        blank=True,
        null=True,)
    
    code = models.CharField(
        max_length=150, blank=True, verbose_name=_("Code")
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    lote = models.CharField(
        max_length=150, blank=True, verbose_name=_("Lote")
    )
    
    def __str__(self):
        return "{}-{}".format(self.product.name, self.lote)

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")