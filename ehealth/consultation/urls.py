
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_meeting, name='create_meeting'),
    path('join/<str:meeting_id>/', views.join_meeting, name='join_meeting'),
]
