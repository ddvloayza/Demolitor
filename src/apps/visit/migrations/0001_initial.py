# Generated by Django 4.1.3 on 2023-04-17 07:21

import apps.product.utils
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("seo_title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "seo_description",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "seo_keywords",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=150, verbose_name="Name"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=apps.product.utils.custom_category_upload_to,
                        verbose_name="image_category",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("seo_title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "seo_description",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "seo_keywords",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=150, verbose_name="Name"),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=apps.product.utils.custom_product_upload_to,
                        verbose_name="image_product",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="product.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
    ]
