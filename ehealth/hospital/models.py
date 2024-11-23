from django.db import models
from accounts.models import User

class Hospital(models.Model):
    """Model for storing hospital information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="hospital_profile")
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    """Model for hospital departments."""
    name = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="departments")

    def __str__(self):
        return f"{self.name} - {self.hospital.name}"

class Patient(models.Model):
    """Model for patient information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_profile")
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="patients")
    age = models.IntegerField()
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    """Model for doctor information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor_profile", null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="doctors")
    license_number = models.CharField(max_length=50, unique=True)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} ({self.specialization})"
