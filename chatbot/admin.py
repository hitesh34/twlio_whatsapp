# chatbot/admin.py

from django.contrib import admin
from .models import ChatConversation

# Register your model with the admin site
admin.site.register(ChatConversation)
