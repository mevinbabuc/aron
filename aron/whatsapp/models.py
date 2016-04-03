from __future__ import unicode_literals
from django.db import models

from subscribe.models import Subscriber


class Outgoing(models.Model):

    to_phone = models.CharField(max_length=16, null=False, blank=False)
    content = models.TextField(blank=False)

    subscriber = models.ForeignKey(Subscriber)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        verbose_name = "Outgoing message"
        verbose_name_plural = "Outgoing messages"

    def __str__(self):
        pass
