from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import SubscriptionCode, Plan
from .forms import GenerateSubscriptionCodeForm, RedeemSubscriptionCodeForm

# Doctor generates subscription code tied to a plan
# @login_required
# def generate_subscription_code(request):
#     if not request.user.is_doctor:  # Ensure only doctors can generate codes
#         messages.error(request, "You are not authorized to generate subscription codes.")
#         return redirect('home')

#     if request.method == 'POST':
#         form = GenerateSubscriptionCodeForm(request.POST)
#         if form.is_valid():
#             subscription_code = form.save(commit=False)
#             subscription_code.created_by = request.user
#             subscription_code.save()
#             messages.success(request, f"Subscription code '{subscription_code.code}' for plan '{subscription_code.plan.name}' created successfully!")
#             return redirect('subscriptions:generate_code')
#     else:
#         form = GenerateSubscriptionCodeForm()

#     return render(request, 'subscriptions/generate_code.html', {'form': form})


def is_doctor(user):
    return user.is_doctor 

@login_required
@user_passes_test(is_doctor)
def generate_subscription_code(request):
    form = GenerateSubscriptionCodeForm()

    if request.method == 'POST':
        
        form = GenerateSubscriptionCodeForm(request.POST)
        if form.is_valid():

            subscription_code = form.save(commit=False)
            subscription_code.created_by = request.user  # Assign the logged-in doctor
            subscription_code.save()
            return render(request, 'subscriptions/generate_code.html', {
                'form': form,
                'generated_code': subscription_code.code,
            })
    else:
        form = GenerateSubscriptionCodeForm()

    return render(request, 'subscriptions/generate_code.html', {'form': form})


# Patient redeems subscription code and is tied to a plan
@login_required
def redeem_subscription_code(request):
    if request.method == 'POST':
        form = RedeemSubscriptionCodeForm(request.POST)
        if form.is_valid():
            code_input = form.cleaned_data['code']
            try:
                subscription_code = SubscriptionCode.objects.get(code=code_input, is_used=False)
                subscription_code.assigned_to = request.user
                subscription_code.is_used = True
                subscription_code.save()
                messages.success(request, f"Subscription successful! You are now subscribed to the '{subscription_code.plan.plan_offer}' plan.")
                return redirect('subscriptions:subscription_details')
            except SubscriptionCode.DoesNotExist:
                messages.error(request, "Invalid or already used subscription code.")
    else:
        form = RedeemSubscriptionCodeForm()

    return render(request, 'subscriptions/redeem_code.html', {'form': form})

# View subscription details
@login_required
def subscription_details(request):
    try:
        subscription_code = request.user.subscription
    except SubscriptionCode.DoesNotExist:
        subscription_code = None

    return render(request, 'subscriptions/subscription_details.html', {'subscription_code': subscription_code})
