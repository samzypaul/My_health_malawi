from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from .forms import ChatMessageForm
from accounts.models import User

@login_required
def chat_view(request, recipient_id):
    """View for chatting with a specific user."""
    recipient = User.objects.get(id=recipient_id)
    messages = ChatMessage.objects.filter(
        sender=request.user, receiver=recipient
    ) | ChatMessage.objects.filter(
        sender=recipient, receiver=request.user
    ).order_by('timestamp')

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = recipient
            message.save()
            return redirect('chat', recipient_id=recipient.id)
    else:
        form = ChatMessageForm()

    return render(request, 'chat/chat.html', {
        'recipient': recipient,
        'messages': messages,
        'form': form,
    })
