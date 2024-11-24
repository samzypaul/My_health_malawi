from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from hospital.models import Doctor,Patient

@login_required
def book_appointment(request):
    """Patient books an appointment."""
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            # Retrieve the Patient instance associated with the logged-in user 
            patient = get_object_or_404(Patient, user=request.user)
            appointment.patient = patient
            #appointment.patient = request.user
            appointment.save()
            return redirect('patient_dashboard')
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})

@login_required
def doctor_appointments(request):
    """Doctor views their appointments."""
    doctor = request.user.doctor_profile
    appointments = doctor.appointments.all().order_by('date', 'time')
    return render(request, 'appointments/doctor_appointments.html', {'appointments': appointments})
