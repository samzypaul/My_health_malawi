from django import forms
from .models import Patient, Doctor

class PatientForm(forms.ModelForm):
    """Form for creating and updating patient records."""
    class Meta:
        model = Patient
        fields = ['hospital', 'age', 'medical_history']

class DoctorForm(forms.ModelForm):
    """Form for creating and updating doctor records."""
    class Meta:
        model = Doctor
        fields = ['hospital', 'department', 'license_number', 'specialization']
