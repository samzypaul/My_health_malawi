from django.urls import path
from . import views
app_name='appointments'
urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('doctor/', views.doctor_appointments, name='doctor_appointments'),
    path('patient/', views.patient_appointments, name='patient_appointments'),
    path('update_status/<int:pk>/', views.update_appointment_status, name='update_status'),
]
