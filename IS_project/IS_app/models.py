from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    paid_subscription = models.BooleanField(default=False)
    subscription_start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.email} - Paid Subscription: {self.paid_subscription}"
