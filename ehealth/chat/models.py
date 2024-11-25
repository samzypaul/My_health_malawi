from django.db import models
from django.conf import settings

# class ChatMessage(models.Model):
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")
#     recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_messages")
#     text = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['timestamp']

#     def __str__(self):
#         return f"Message from {self.sender} to {self.recipient} at {self.timestamp}"



class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='sent_messages'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='received_messages'
    )
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.recipient}: {self.message_text[:30]}"
