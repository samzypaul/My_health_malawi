from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('doctor_chat/',views.doctor_chat, name='doctor_chat'),
    path('patient_chat/',views.patient_chat, name='patient_chat'),
    path('<int:recipient_id>/', views.chat_view, name='chat_view'),
    path('send_message/', views.send_message, name='send_message'),
]
