from django.db import models
from django.conf import settings

class FriendRequest(models.Model):
    STATUS_CHOICES = (
        ('sent', 'Sent'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='sent')
    
    class Meta:
        unique_together = ('from_user', 'to_user')  # Prevent duplicate requests

    def __str__(self):
        return f"{self.from_user} -> {self.to_user}: {self.status}"