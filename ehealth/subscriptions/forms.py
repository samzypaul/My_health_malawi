from django import forms
from .models import SubscriptionCode, Plan
import random
import string

class GenerateSubscriptionCodeForm(forms.ModelForm):
    plan = forms.ModelChoiceField(queryset=Plan.objects.all(), required=True)

    class Meta:
        model = SubscriptionCode
        fields = ['plan']

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Generate a random 10-character subscription code
        instance.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        
        if commit:
            instance.save()
        return instance



class RedeemSubscriptionCodeForm(forms.Form):
    code = forms.CharField(max_length=10, label="Enter Subscription Code")

