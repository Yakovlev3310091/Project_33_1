from rest_framework import serializers

from bot.models import TgUser
from bot.tg.client import TgClient


class TgUserVerCodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = "__all__"
        read_only_fields = ("id", "chat_id", "user_ud")

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        TgClient.send_message(chat_id=instance.chat_id, text="Успешно")
        return instance
    