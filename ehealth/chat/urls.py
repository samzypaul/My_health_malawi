from django.urls import path
from . import views

urlpatterns = [
    path('<int:recipient_id>/', views.chat_view, name='chat'),
]
