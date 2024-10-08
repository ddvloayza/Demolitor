# Generated by Django 4.1.3 on 2023-10-10 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ubigeos", "0002_auto_20210325_1040"),
        ("company", "0004_alter_company_contacts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="distrito",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ubigeos.distrito",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="provincia",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ubigeos.provincia",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="region",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ubigeos.region",
            ),
        ),
    ]
