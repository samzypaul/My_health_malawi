from django.shortcuts import render, get_object_or_404, redirect
from django.utils.crypto import get_random_string
from .models import Meeting
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def create_meeting(request):
    """Create a new video meeting."""
    if request.method == 'POST':
        meeting_id = get_random_string(length=10)
        meeting = Meeting.objects.create(
            host=request.user,
            meeting_id=meeting_id,
            start_time=request.POST.get('start_time'),
            duration_minutes=request.POST.get('duration_minutes')
        )
        return redirect('join_meeting', meeting_id=meeting.meeting_id)
    return render(request, 'consultation/create_meeting.html')

@login_required
def join_meeting(request, meeting_id):
    """Join an existing meeting."""
    meeting = get_object_or_404(Meeting, meeting_id=meeting_id)
    if request.user not in meeting.participants.all() and request.user != meeting.host:
        return HttpResponseForbidden("You are not allowed to join this meeting.")
    return render(request, 'consultation/join_meeting.html', {'meeting': meeting})