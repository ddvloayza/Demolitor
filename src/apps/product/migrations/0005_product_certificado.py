# Generated by Django 4.1.3 on 2023-06-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_category_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="certificado",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="certificados/",
                verbose_name="certificado",
            ),
        ),
    ]
