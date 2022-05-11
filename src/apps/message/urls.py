from django.urls import path

from . import views

urlpatterns = [
    path("v1/message/", views.MessageCreateView.as_view(), name="message-create"),
    path("v1/message_confirmation/", views.MessageConfirmView.as_view(), name="message-confirm"),
]
