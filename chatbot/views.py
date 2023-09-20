# chatbot/views.py
from twilio.rest import Client
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatConversation
from .serializers import ChatConversationSerializer


@api_view(['POST'])
def send_message(request):
    from_whatsapp_number = settings.TWILIO_FROM_WHATSAPP_NUMBER
    to_whatsapp_number = request.data.get('to_whatsapp_number', '')
    message_body = request.data.get('message_body', '')

    if not to_whatsapp_number or not message_body:
        return Response({'error': 'to_whatsapp_number and message_body are required.'}, status=400)

    # Send the message using Twilio
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message_body,
        from_=from_whatsapp_number,
        to=to_whatsapp_number,
    )

    # Create or update the ChatConversation object
    conversation, created = ChatConversation.objects.get_or_create(
        from_whatsapp_number=from_whatsapp_number,
        to_whatsapp_number=to_whatsapp_number,
    )
    conversation.messages += f"\nOutgoing: {message_body}"
    conversation.save()

    serializer = ChatConversationSerializer(conversation)

    return Response(serializer.data, status=200)


@api_view(['POST'])
def respond_to_message(request):
    from_whatsapp_number = request.data.get('from_whatsapp_number', '')
    to_whatsapp_number = settings.TWILIO_FROM_WHATSAPP_NUMBER
    message_body = request.data.get('message_body', '')

    if not from_whatsapp_number or not message_body:
        return Response({'error': 'from_whatsapp_number and message_body are required.'}, status=400)

    # Create or update the ChatConversation object
    conversation, created = ChatConversation.objects.get_or_create(
        from_whatsapp_number=from_whatsapp_number,
        to_whatsapp_number=to_whatsapp_number,
    )

    conversation.response = message_body

    conversation.messages += f"\nIncoming: {message_body}"
    conversation.save()

    serializer = ChatConversationSerializer(conversation)

    return Response(serializer.data, status=200)
