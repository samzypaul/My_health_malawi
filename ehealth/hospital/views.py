from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hospital, Patient, Doctor, Department
from .forms import PatientForm, DoctorForm

@login_required
def patient_dashboard(request):
    """Patient dashboard view."""
    patient = request.user.patient_profile
    return render(request, 'hospital/patient_dashboard.html', {'patient': patient})

@login_required
def doctor_dashboard(request):
    """Doctor dashboard view."""
    doctor = request.user.doctor_profile
    return render(request, 'hospital/doctor_dashboard.html', {'doctor': doctor})

@login_required
def hospital_dashboard(request):
    """Hospital dashboard for administrators."""
    hospital = get_object_or_404(Hospital, doctors__user=request.user)
    patients = hospital.patients.all()
    doctors = hospital.doctors.all()
    return render(request, 'hospital/hospital_dashboard.html', {
        'hospital': hospital,
        'patients': patients,
        'doctors': doctors
    })




#patient views dashboard


@login_required
def patient_home(request):
    return render(request, '/patient_dashboard.html', {'active_tab': 'home'})

@login_required
def patient_departments(request):
    return render(request, '/patient_dashboard.html', {'active_tab': 'departments'})

@login_required
def patient_consultation(request):
    return render(request, '/patient_dashboard.html', {'active_tab': 'consultation'})

@login_required
def patient_health_records(request):
    return render(request, '/patient_dashboard.html', {'active_tab': 'health_records'})

@login_required
def patient_subscription(request):
    return render(request, '/patient_dashboard.html', {'active_tab': 'subscription'})


# doctors dashboard views
from appointments.models import Appointment
#from utils.code_generators import generate_subscription_code
from . import helper as generate_subscription_code


@login_required
def doctor_home(request):
    return render(request, 'hospital/doctor_dashboard.html', {'active_tab': 'home'})

@login_required
def doctor_patients(request):
    # Fetch patients linked to this doctor
    patients = Patient.objects.filter(doctor=request.user.doctor)
    return render(request, 'hospital/doctor_dashboard.html', {'active_tab': 'patients', 'patients': patients})

@login_required
def doctor_appointments(request):
    # Fetch appointments linked to this doctor
    appointments = Appointment.objects.filter(doctor=request.user.doctor)
    return render(request, 'hospital/doctor_dashboard.html', {'active_tab': 'appointments', 'appointments': appointments})

@login_required
def doctor_subscription(request):
    if request.method == 'POST':
        # Generate a unique subscription code
        subscription_code = generate_subscription_code(request.user.doctor)
        return render(request, 'hospital/doctor_dashboard.html', {'active_tab': 'subscription', 'subscription_code': subscription_code})
    return render(request, 'hospital/doctor_dashboard.html', {'active_tab': 'subscription'})


#hospital views


@login_required
def hospital_home(request):
    return render(request, 'hospital/hospital_dashboard.html', {'active_tab': 'home'})

@login_required
def hospital_manage_doctors(request):
    doctors = Doctor.objects.filter(hospital=request.user.hospitaladmin.hospital)
    return render(request, 'hospital/hospital_dashboard.html', {'active_tab': 'manage_doctors', 'doctors': doctors})

@login_required
def hospital_manage_patients(request):
    patients = Patient.objects.filter(hospital=request.user.hospitaladmin.hospital)
    return render(request, 'hospital/hospital_dashboard.html', {'active_tab': 'manage_patients', 'patients': patients})

@login_required
def hospital_analytics(request):
    # Example analytics data
    total_patients = Patient.objects.filter(hospital=request.user.hospitaladmin.hospital).count()
    total_doctors = Doctor.objects.filter(hospital=request.user.hospitaladmin.hospital).count()
    return render(request, 'hospital/hospital_dashboard.html', {
        'active_tab': 'analytics',
        'total_patients': total_patients,
        'total_doctors': total_doctors
    })
