# Generated by Django 5.1.1 on 2024-10-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0018_alter_product_image_productimage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productimage",
            options={
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.AddField(
            model_name="productimage",
            name="order",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
