from django.db import models
from accounts.models import User

class Meeting(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host_meetings')
    participants = models.ManyToManyField(User, related_name='meetings')
    meeting_id = models.CharField(max_length=50, unique=True)
    start_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"Meeting {self.meeting_id} hosted by {self.host.username}"
