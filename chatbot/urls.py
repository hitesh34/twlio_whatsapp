from django.urls import path
from .views import send_message, respond_to_message, whatsapp_webhook

urlpatterns = [
    path('send-message/', send_message, name='send-message'),
    path('respond-to-message/', respond_to_message, name='respond-to-message'),
    path('whatsapp-webhook/', whatsapp_webhook,
         name='whatsapp-webhook'),  # Add this line
]
