from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm,AppointmentStatusUpdateForm
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
            #patient = Patient.objects.get_or_create(user=request.user)
            appointment.patient = patient
            appointment.save()
            return redirect('hospital:patient_dashboard')
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})

@login_required
def doctor_appointments(request):
    """Doctor views their appointments."""
    doctor = request.user.doctor_profile
    appointments = doctor.appointments.all().order_by('date', 'time')
    return render(request, 'doctor_appointments.html', {'appointments': appointments})


@login_required
def patient_appointments(request):
    """Patient views their appointments."""
    patient = request.user.patient_profile
    appointments = patient.appointments.all().order_by('date', 'time')
    return render(request, 'patient_appointments.html', {'appointments': appointments})


def update_appointment_status(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentStatusUpdateForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments:doctor_appointments')  # Redirect back to doctor dashboard or appointments page
    else:
        form = AppointmentStatusUpdateForm(instance=appointment)
    return render(request, 'update_status.html', {'form': form, 'appointment': appointment})
