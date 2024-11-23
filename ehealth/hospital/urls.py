from django.urls import path
from . import views

urlpatterns = [
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('hospital/dashboard/', views.hospital_dashboard, name='hospital_dashboard'),
#patient dashboard urls
  
    path('dashboard/patient/', views.patient_home, name='patient_home'),
    path('dashboard/patient/departments/', views.patient_departments, name='patient_departments'),
    path('dashboard/patient/consultation/', views.patient_consultation, name='patient_consultation'),
    path('dashboard/patient/health_records/', views.patient_health_records, name='patient_health_records'),
    path('dashboard/patient/subscription/', views.patient_subscription, name='patient_subscription'),

    #doctor dashboard urls
     path('dashboard/doctor/', views.doctor_home, name='doctor_home'),
    path('dashboard/doctor/patients/', views.doctor_patients, name='doctor_patients'),
    path('dashboard/doctor/appointments/', views.doctor_appointments, name='doctor_appointments'),
    path('dashboard/doctor/subscription/', views.doctor_subscription, name='doctor_subscription'),

    #hospital dashboard urls
     path('dashboard/hospital/', views.hospital_home, name='hospital_home'),
    path('dashboard/hospital/manage-doctors/', views.hospital_manage_doctors, name='hospital_manage_doctors'),
    path('dashboard/hospital/manage-patients/', views.hospital_manage_patients, name='hospital_manage_patients'),
    path('dashboard/hospital/analytics/', views.hospital_analytics, name='hospital_analytics'),
]



