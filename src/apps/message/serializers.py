from rest_framework import serializers

from .models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "text")


class MessageConfirmSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    success = serializers.BooleanField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
