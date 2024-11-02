from django.db import models
from users.models import Users


class PrivateChat(models.Model):
    owner_chat = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE,
        related_name='owner_chat'
    )
    name = models.CharField(max_length=20)
    users = models.ManyToManyField(
        to=Users,
        related_name='users',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
    
class PrivateMessages(models.Model):
    owner_message = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    where_message = models.ForeignKey(
        to=PrivateChat,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name