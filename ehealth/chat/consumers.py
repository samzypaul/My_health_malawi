from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json
from .models import Message, User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # Join the chat group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the chat group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender_id = data['sender']
        recipient_id = data['recipient']

        # Save the message to the database
        await self.save_message(sender_id, recipient_id, message)

        # Send the message to the chat group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender_id,
            }
        )

        # Notify the recipient of a new message
        await self.channel_layer.group_send(
            f"notifications_{recipient_id}",
            {
                'type': 'notify_new_message',
            }
        )

    async def chat_message(self, event):
        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))

    @sync_to_async
    def save_message(self, sender_id, recipient_id, message_text):
        sender = User.objects.get(id=sender_id)
        recipient = User.objects.get(id=recipient_id)
        Message.objects.create(sender=sender, recipient=recipient, message_text=message_text)


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.group_name = f"notifications_{self.user_id}"

        # Join the notifications group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the notifications group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def notify_new_message(self, event):
        # Send a notification to WebSocket
        await self.send(text_data=json.dumps({
            'new_message': True,
        }))
