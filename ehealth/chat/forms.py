from django import forms
from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    """Form for sending messages."""
    class Meta:
        model = ChatMessage
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your message...',
                'rows': 2,
            })
        }
