from django.db import models


class SEOMixin(models.Model):

    seo_title = models.CharField(max_length=100, null=True, blank=True)

    seo_description = models.CharField(max_length=150, null=True, blank=True)

    seo_keywords = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True
