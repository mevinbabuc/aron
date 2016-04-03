from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Subscriber(models.Model):

    user = models.OneToOneField(User, help_text='Details of the user')
    channels = models.ManyToManyField('Channel', help_text='Different channels the user is subscribed to')
    phone = models.CharField(max_length=16, null=False, blank=False, help_text='The unique phone number of the user')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        pass


class Channel(models.Model):

    name = models.CharField(max_length=64, null=False, blank=False, help_text='The name of the channel')
    description = models.TextField(null=False, help_text='A short description of what the user can expect by subscribing to this channel')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        pass


class Message(models.Model):

    data = models.TextField(blank=False, null=False)
    channel = models.ForeignKey(Channel)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        pass
    