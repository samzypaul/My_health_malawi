from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from . models import User
from django.db import IntegrityError
from . import forms
from . forms import CustomAuthentificationForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

# def register(request):
#     template = loader.get_template('register.html')
#     if request.method == 'POST':
#         form = forms.CustomUserCreationForm(request.POST)
#         try:
#             if form.is_valid():
#                 form.save()
#                 # login(request, form.get_user())
#                 messages.success(request, 'Registration successful!')
#                 return redirect('accounts:login')
#             else:
#                 messages.error(request, 'Please correct the errors below.')
#         #except IntegrityError:
#         except IntegrityError:
#             messages.error(request, 'Username already exists. Please choose a different username.')
#     else:
#         form = forms.CustomUserCreationForm()
    
#     context = {
#         'form': form,
#     }
#     return HttpResponse(template.render(context, request))


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthentificationForm  

# def login_user(request):
#     template = 'login.html'
#     context = {'form': CustomAuthentificationForm()}

#     if request.method == 'POST':
#         form = CustomAuthentificationForm(request, request.POST)
#         if form.is_valid():


#             user = form.get_user()  #authenticate(request, email=email, password=password)
#             if user is not None:
#                 print('hie')
#                 login(request, user)
#                 # Redirect based on user role 
#                 if user.is_superuser:  # Check for admin role
#                     print('admin')
#                     return redirect('/admin')
#                 elif user.is_staff:
#                     print('doctor')
#                     return redirect('/accountsregister')  # Default redirect for other users
#                 else:
#                     print(f'patient')
#                     return redirect('/patientsd_patients')


#             else:
#                 print('invalid form')
#                 # Authentication failed:
#                 context['error_message'] = 'Invalid credentials. Please check your username/email and password.'  # Set a more informative error message

#     return render(request, template, context)

def login_user(request):
    context = {'form': CustomAuthentificationForm()}

    if request.method == 'POST':
        form = CustomAuthentificationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                # Redirect based on user role 
                if user.is_superuser:  # Superuser role
                    return redirect('/admin')
                elif user.is_staff:  # Doctor role
                    return redirect('doctor_dashboard')  # Use a valid URL name for doctor dashboard
                else:  # Patient role
                    return redirect('patient_dashboard')  # Use a valid URL name for patient dashboard
            else:
                context['error_message'] = 'Invalid credentials. Please check your username/email and password.'

    return render(request, 'login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/accountslogin')

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def contact_us(request):
    template = loader.get_template('contact_us.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send an email (optional, requires proper email backend setup)
        send_mail(
            subject=f"New Contact Us Message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],  # Replace with your email
        )

        return HttpResponse("<h3>Thank you for contacting us. We'll get back to you shortly.</h3>")
    context = {}
    return render(request,'contact_us.html')#HttpResponse(template.render(request, context))#, '/accounts/contact_us.html')
def test_template(request):
    return render(request, 'register.html')
