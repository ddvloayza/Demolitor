# Generated by Django 5.1.1 on 2024-10-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0022_productimage_is_info_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="content",
        ),
        migrations.AddField(
            model_name="product",
            name="is_best_seller",
            field=models.BooleanField(default=False, verbose_name="Best Seller"),
        ),
        migrations.AddField(
            model_name="product",
            name="price_discount",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                max_digits=18,
                verbose_name="price_discount",
            ),
        ),
    ]
