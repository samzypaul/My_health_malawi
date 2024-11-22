from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from . models import User
from django.db import IntegrityError
from . import forms
from . forms import CustomAuthentificationForm
from django.contrib.auth.decorators import login_required


def register(request):
    template = loader.get_template('register.html')
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                # login(request, form.get_user())
                messages.success(request, 'Registration successful!')
                return redirect('accounts:login')
            else:
                messages.error(request, 'Please correct the errors below.')
        #except IntegrityError:
        except IntegrityError:
            messages.error(request, 'Username already exists. Please choose a different username.')
    else:
        form = forms.CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthentificationForm  

def login_user(request):
    template = 'login.html'
    context = {'form': CustomAuthentificationForm()}

    if request.method == 'POST':
        form = CustomAuthentificationForm(request, request.POST)
        if form.is_valid():


            user = form.get_user()  #authenticate(request, email=email, password=password)
            if user is not None:
                print('hie')
                login(request, user)
                # Redirect based on user role 
                if user.is_superuser:  # Check for admin role
                    print('admin')
                    return redirect('/admin')
                elif user.is_staff:
                    print('doctor')
                    return redirect('/accountsregister')  # Default redirect for other users
                else:
                    print(f'patient')
                    return redirect('/patientsd_patients')


            else:
                print('invalid form')
                # Authentication failed:
                context['error_message'] = 'Invalid credentials. Please check your username/email and password.'  # Set a more informative error message

    return render(request, template, context)



@login_required
def logout_user(request):
    logout(request)
    return redirect('/accountslogin')