from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('email', 'first_name', 'last_name', 'username', 'phone_number', 'role','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control bg-transparent w-[400px] px-2 py-2 border-2 border-gray-500 rounded-lg', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-transparent w-[400px] px-2 py-2 border-2 border-gray-500 rounded-lg', 'placeholder':'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control bg-transparent w-[400px] px-2 py-2 border-2 border-gray-500 rounded-lg', 'placeholder':'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control bg-transparent w-[400px] px-2 py-2 border-2 border-gray-500 rounded-lg', 'placeholder':'Last Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control bg-transparent w-[400px] px-2 py-2 border-2 border-gray-500 rounded-lg', 'placeholder':'Phone No.'}),
            'role': forms.Select(attrs={'class': 'form-control bg-transparent w-[400px] px-2 py-2 border-2 border-gray-500 rounded-lg', 'placeholder':'Select Role'}),
            'password1': forms.Select(attrs={'class': 'form-control bg-transparent w-[400px] px-2 py-2 border-2 border-gray-500 rounded-lg', 'placeholder':'Enter Password'}),
            'password2': forms.Select(attrs={'class': 'form-control bg-transparent w-[400px] px-2 py-2 border-2 border-gray-500 rounded-lg', 'placeholder':'Confirm Password'}),
        }

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if password1 and password2 and password1 != password2:
                raise ValidationError('Passwords don\'t match')
            return password2 
        

class CustomAuthentificationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = models.User.objects.filter(Q(username=username) | Q(email=username)).first()

            if user is None:
                raise forms.ValidationError('Invalid username or email')
            elif not user.check_password(password):
                raise forms.ValidationError('Invalid password')

        return self.cleaned_data


