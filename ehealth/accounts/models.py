from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)  # Use username or email based on your setup

    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Emails are required!')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username.lower(),  # Enforce lowercase usernames (optional)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    DOCTOR = 2
    PATIENT = 3

    ROLE_CHOICE = (
        (ADMIN, 'admin'),
        (DOCTOR, 'doctor'),
        (PATIENT, 'patient'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # Use username or email for authentication based on your setup
    username = models.CharField(max_length=50, unique=True)  # Optional if using email
    email = models.EmailField(unique=True)  # Required for email authentication

    phone_number = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, default=3)

    # Django required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} {self.first_name} {self.last_name} {self.phone_number}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
