import json

import requests
from django.conf import settings
from kafka import KafkaConsumer

from . import services

consumer = KafkaConsumer(
    "message",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="my-group-id",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

url = f"{settings.ROOT_URL}/api/v1/message_confirmation/"


def checker():
    messages = (msg for msg in consumer)
    while True:
        try:
            message = next(messages)
            message_id, message_text = message.value.values()

            requests.post(
                url,
                {"id": message_id, "success": services.abracadabra_in_message(message_text)},
                headers={"authorization": settings.CONFIRM_AUTH_KEY},
            )
        except ValueError as e:
            print(e)
            break
