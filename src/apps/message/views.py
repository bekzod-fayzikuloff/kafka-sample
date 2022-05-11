from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from .models import Message
from .serializers import MessageConfirmSerializer, MessageCreateSerializer


class MessageCreateView(GenericAPIView):
    serializer_class = MessageCreateSerializer

    def post(self, request: HttpRequest) -> Response:
        serializer = self.serializer_class(data=self.request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class MessageConfirmView(GenericAPIView):
    serializer_class = MessageConfirmSerializer

    def post(self, request: HttpRequest) -> Response:

        if self.request.headers.get("authorization") != settings.CONFIRM_AUTH_KEY:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=self.request.POST)
        if serializer.is_valid():
            message_id, message_status = serializer.data.values()
            message = get_object_or_404(Message, pk=message_id)

            message.status = Message.MessageStatus.CORRECT if message_status else Message.MessageStatus.BLOCKED
            message.save()

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
