from django.db import models


class Message(models.Model):
    class MessageStatus(models.TextChoices):
        REVIEW = ("Rev", "Review")
        BLOCKED = ("Blo", "Blocked")
        CORRECT = ("Cor", "Correct")

    text = models.TextField()
    status = models.CharField(max_length=3, choices=MessageStatus.choices, default=MessageStatus.REVIEW)

    def __str__(self):
        return f"{self.id}<->{self.get_status_display()}"

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
