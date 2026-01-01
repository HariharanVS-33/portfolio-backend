from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactMessageSerializer
from django.conf import settings

@api_view(['POST'])
def create_contact_message(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        message_obj = serializer.save()

        send_mail(
            subject="New Contact Message",
            message=f"""
Name: {message_obj.name}
Email: {message_obj.email}

Message:
{message_obj.message}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return Response(
            {"message": "Message sent successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)