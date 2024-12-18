# Generated by Django 5.1.1 on 2024-11-24 03:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0026_product_skill_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="KeyFeature",
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
                ("name", models.CharField(max_length=255, verbose_name="Key Feature")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="product",
            name="rating",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                help_text="Product rating (e.g., 0.00 to 5.00).",
                max_digits=3,
                verbose_name="Rating",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="key_features",
            field=models.ManyToManyField(
                blank=True,
                related_name="products",
                to="product.keyfeature",
                verbose_name="Key Features",
            ),
        ),
    ]
