from django.db import models


class ChatConversation(models.Model):
    from_whatsapp_number = models.CharField(max_length=20)
    to_whatsapp_number = models.CharField(max_length=20)
    messages = models.TextField(default="Welcome to HomeOpen")
    date_created = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)
