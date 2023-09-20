# chatbot/urls.py

from django.urls import path
from .views import send_message, respond_to_message  # Remove the import for view_conversation

urlpatterns = [
    path('send-message/', send_message, name='send-message'),
    path('respond-to-message/', respond_to_message, name='respond-to-message'),  # Update the URL pattern
]
