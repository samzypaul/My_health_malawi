from django.db import models
from django.conf import settings  # settings to reference AUTH_USER_MODEL dynamically
from hospital.models import Hospital

class Plan(models.Model):
    PLANS_OFFERED = (
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum')
    )
    plan_offer = models.CharField(max_length=50, choices=PLANS_OFFERED, blank=False, default='Silver')
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, related_name="plan")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.plan_offer} Plan at {self.hospital.name}"

class SubscriptionCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='subscription_codes')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='created_codes'
    )  # Doctor
    assigned_to = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='subscription'
    )  # Patient
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Code: {self.code} Plan: {self.plan.plan_offer} Used: {self.is_used}"
