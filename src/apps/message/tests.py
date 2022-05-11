from django.conf import settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from .models import Message


class TestMessageCreateView(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_message_create__correct_case(self):
        """
        Test message create
        Permission : anyone
        """
        # POST /api/v1/message/
        url = reverse("message-create")
        data = {"text": "true"}

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["text"], data["text"])

    def test_message_create__unsupported_fields(self):
        """
        Test message create
        Permission : anyone
        """
        # POST /api/v1/message/
        url = reverse("message-create")
        data = {"not_valid_field": "some value"}

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestMessageConfirmView(APITestCase):
    def setUp(self) -> None:
        Message.objects.bulk_create([Message(text="some text") for _ in range(5)])
        self.url = reverse("message-confirm")

    def test_message_confirm__without_credentials(self):
        """
        Test message confirmation
        Permission : Lister
        """
        # POST /api/v1/message_confirmation/

        data = {"id": 1, "success": "true"}
        # 1. Request without authorization header (incorrect case too)

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_message_confirm__with_credentials(self):
        # 2. Request with authorization header and not exits message change case
        data = {"id": 25, "success": True}

        self.client.credentials(HTTP_AUTHORIZATION=settings.CONFIRM_AUTH_KEY)
        response = self.client.post(self.url, data=data, Authorization=settings.CONFIRM_AUTH_KEY)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_confirm_correct_case(self):

        data = {"id": 1, "success": True}
        self.client.credentials(HTTP_AUTHORIZATION=settings.CONFIRM_AUTH_KEY)
        response = self.client.post(
            self.url,
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
