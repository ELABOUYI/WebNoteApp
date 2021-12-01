from django.db import models


class Note(models.Model):
    note = models.CharField(max_length=180)

    class Meta:
        verbose_name = 'note'
        verbose_name_plural = 'notes'
