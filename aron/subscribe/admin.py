from django.contrib import admin
from .models import Subscriber, Channel, Message
# Register your models here.

admin.site.register(Subscriber)
admin.site.register(Channel)
admin.site.register(Message)
