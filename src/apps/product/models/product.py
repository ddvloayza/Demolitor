from django.db import models
from apps.core.models.base import BaseModelMixin
from apps.core.models.seo import SEOMixin
from apps.product.schema.enums.enums import ObjectiveChoices
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


class KeyFeature(BaseModelMixin):
    name = models.CharField(max_length=255, verbose_name=_("Key Feature"))

    def __str__(self):
        return self.name
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
    price_discount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00,
        verbose_name="price_discount",
    )
    is_best_seller = models.BooleanField(default=False, verbose_name="Best Seller")

    tag = models.ManyToManyField("tag.Tag", verbose_name=_("Tags"), blank=True, related_name="product_tags")
    flavors = models.ManyToManyField('Flavor', related_name="products", blank=True)
    packagings = models.ManyToManyField('Packaging', related_name="products", blank=True)
    skill_tags = models.ManyToManyField('tag.SkillTag', related_name="skill_tag_products", blank=True)

    objective = models.CharField(
        max_length=200,
        choices=ObjectiveChoices.choices,
        default=ObjectiveChoices.FITNESS,
        verbose_name="Objetivo"
    )
    # Nuevo campo para puntuación
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.00,
        verbose_name=_("Rating"),
        help_text=_("Product rating (e.g., 0.00 to 5.00).")
    )

    # Nuevo campo para características claves
    key_features = models.ManyToManyField(
        KeyFeature,
        related_name="products",
        blank=True,
        verbose_name=_("Key Features")
    )


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


class FAQ(BaseModelMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="faqs"  # Allows reverse access from Product to its FAQs
    )
    question = models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    suggestion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.question} ({self.product.name})"


class Characteristic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="characteristics")
    feature_name = models.CharField(max_length=100, verbose_name="Feature Name", blank=True, null=True)
    feature_value = models.CharField(max_length=200, verbose_name="Feature Value", blank=True, null=True)
    is_key_feature = models.BooleanField(default=False, verbose_name="Is Key Feature")  # Added boolean field

    def __str__(self):
        return f"{self.feature_name}: {self.feature_value} (Key: {self.is_key_feature})"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.FileField(
        verbose_name=_("Product File"),
        upload_to=custom_product_upload_to,
        blank=True,
        null=True,
    )
    order = models.PositiveSmallIntegerField()
    is_info_image = models.BooleanField(default=False, verbose_name="Is Info Image")
    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")


class Flavor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Flavor Name")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Flavor")
        verbose_name_plural = _("Flavors")


class Packaging(models.Model):
    size = models.CharField(max_length=50, verbose_name="Size or Packaging")  # Example: 1kg, 500ml
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Packaging Price")

    def __str__(self):
        return f"{self.size}"

    class Meta:
        verbose_name = _("Packaging")
        verbose_name_plural = _("Packagings")