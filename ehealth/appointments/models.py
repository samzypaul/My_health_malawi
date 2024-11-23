from django.db import models
from hospital.models import Doctor, Patient

class Appointment(models.Model):
    """Model for scheduling appointments."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')],
        default='Pending',
    )

    def __str__(self):
        return f"Appointment with {self.doctor.user.get_full_name} on {self.date} at {self.time}"
