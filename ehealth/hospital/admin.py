from django.contrib import admin
from .models import Hospital, Department, Patient, Doctor

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    search_fields = ['name', 'email']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'hospital']
    search_fields = ['name', 'hospital__name']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'hospital', 'age']
    search_fields = ['user__username', 'hospital__name']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'hospital', 'specialization']
    search_fields = ['user__username', 'hospital__name', 'specialization']
