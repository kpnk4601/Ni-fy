from django.contrib.auth.models import User
from django.db import models
import random
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        """Generate a random 6-digit OTP code."""
        self.otp_code = f"{random.randint(100000, 999999)}"
        self.is_verified = False
        self.save()

    def is_expired(self):
        """Check if the OTP has expired (e.g., after 5 minutes)."""
        return self.created_at + timedelta(minutes=5) < timezone.now()
