from django.urls import path
from chat.consumers import ChatConsumer, NotificationConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
    path('ws/chat/notifications/<int:user_id>/', NotificationConsumer.as_asgi()),
]
