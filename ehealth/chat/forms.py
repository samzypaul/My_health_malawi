from django import forms
from .models import Message

# class ChatMessageForm(forms.ModelForm):
#     """Form for sending messages."""
#     class Meta:
#         model = ChatMessage
#         fields = ['message']
#         widgets = {
#             'message': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Type your message...',
#                 'rows': 2,
#             })
#         }



from chat.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message_text']  # Adjust field names to match your model
        widgets = {
            'message_text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Type your message here...'}),
        }
