from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
class PushSubscription(models.Model):
    subscription = models.TextField()  # stores JSON
    created_at = models.DateTimeField(auto_now_add=True)