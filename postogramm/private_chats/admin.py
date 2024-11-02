from django.contrib import admin
from .models import PrivateChat, PrivateMessages

admin.site.register(PrivateMessages)
admin.site.register(PrivateChat)