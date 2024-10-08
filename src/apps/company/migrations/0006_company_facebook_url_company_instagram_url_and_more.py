# Generated by Django 5.0 on 2024-08-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0005_alter_company_distrito_alter_company_provincia_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="facebook_url",
            field=models.URLField(blank=True, null=True, verbose_name="Facebook URL"),
        ),
        migrations.AddField(
            model_name="company",
            name="instagram_url",
            field=models.URLField(blank=True, null=True, verbose_name="Instagram URL"),
        ),
        migrations.AddField(
            model_name="company",
            name="tiktok_url",
            field=models.URLField(blank=True, null=True, verbose_name="TikTok URL"),
        ),
        migrations.AddField(
            model_name="company",
            name="whatsapp_url",
            field=models.URLField(blank=True, null=True, verbose_name="Whatsapp URL"),
        ),
    ]
