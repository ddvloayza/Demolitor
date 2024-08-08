from django.db import models


class RemovedQuerySet(models.QuerySet):
    def removed(self):
        return self.filter(is_removed=False)


class RemovedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_removed=False)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
