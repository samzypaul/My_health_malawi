from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from accounts.models import User  
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from django.contrib import messages
from chat.forms import MessageForm
from django.core.paginator import Paginator


@login_required

def chat_view(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    recipient_role = recipient.role

    # Fetch all chat messages between the current user and the recipient
    all_messages = Message.objects.filter(
        sender=request.user, recipient=recipient
    ) | Message.objects.filter(
        sender=recipient, recipient=request.user
    ).order_by('timestamp')

    # Handle pagination
    paginator = Paginator(all_messages, 4)  # Show 4 messages per page
    page_number = request.GET.get('page', paginator.num_pages)  # Default to the last page

    # Get the messages for the current page
    messages = paginator.get_page(page_number)

    # Handle message sending
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Save the message
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('chat:chat_view', recipient_id=recipient.id)
    else:
        form = MessageForm()

    # Determine which template to render based on recipient role
    template = 'chat_patient_view.html' if recipient_role == 'doctor' else 'chat_doctor_view.html'

    return render(request, template, {
        'recipient': recipient,
        'messages': messages,  # Paginated messages
        'form': form,
        'paginator': paginator,  # Paginator object to handle pagination in the template
    })
# def chat_view(request, recipient_id):
#     recipient = get_object_or_404(User, id=recipient_id)
#     recipient_role = recipient.role

#     # Restrict chat based on user roles (optional logic can be uncommented if needed)
#     # if request.user.role == 'Doctor' and recipient.role != 'Patient':
#     #     return render(request, 'error.html', {'message': 'You can only chat with patients.'})
#     # elif request.user.role == 'Patient' and recipient.role != 'Doctor':
#     #     return render(request, 'error.html', {'message': 'You can only chat with doctors.'})

#     # Fetch all chat messages between the current user and the recipient
#     all_messages = Message.objects.filter(
#         sender=request.user, recipient=recipient
#     ) | Message.objects.filter(
#         sender=recipient, recipient=request.user
#     ).order_by('timestamp')

#     # Handle pagination for messages
#     paginator = Paginator(all_messages, 4)  # Show 4 messages per page
#     show_older = request.GET.get('show_older', False)
    
#     if show_older:
#         # Show the first page (older messages)
#         page_number = 1
#     else:
#         # Show the last page (latest messages)
#         page_number = paginator.num_pages
    
#     messages = paginator.get_page(page_number)

#     # Handle message sending
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             # Save the message
#             message = form.save(commit=False)
#             message.sender = request.user
#             message.recipient = recipient
#             message.save()
#             return redirect('chat:chat_view', recipient_id=recipient.id)
#     else:
#         form = MessageForm()

#     # Determine which template to render based on recipient role
#     template = 'chat_patient_view.html' if recipient_role == 'doctor' else 'chat_doctor_view.html'

#     return render(request, template, {
#         'recipient': recipient,
#         'messages': messages,  # Paginated messages
#         'form': form,
#         'older_messages_exist': page_number > 1,  # Flag to show older messages button
#     })

@login_required
def doctor_chat(request):
    patients = User.objects.filter(role='patient') 
    for patient in patients:
        print(f'patient:{patient.get_full_name()}')
    return render(request,'doctor_chat.html', {'patients': patients})


@login_required
def patient_chat(request):
    doctors = User.objects.filter(role='doctor') 
    for doctor in doctors:
        print(f'doctor:{doctor.get_full_name()}')
    return render(request, 'patient_chat.html', {'doctors': doctors})



@login_required
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        sender = request.user
        recipient_id = request.POST.get('recipient_id')
        text = request.POST.get('text')

        recipient = get_object_or_404(User, id=recipient_id)
        message = Message.objects.create(sender=sender, recipient=recipient, text=text)

        return JsonResponse({'status': 'success', 'message': message.text, 'timestamp': message.timestamp})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

