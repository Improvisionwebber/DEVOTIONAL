from pywebpush import webpush
from django.conf import settings
import json
from .models import PushSubscription

def send_push_notification(title, body, url="/"):
    subscriptions = PushSubscription.objects.all()
    for sub in subscriptions:
        subscription_info = json.loads(sub.subscription)
        try:
            webpush(
                subscription_info=subscription_info,
                data=json.dumps({
                    "Daily Devotional": title, 
                    "The Devotional is now released": body, 
                    "url": url}),
                vapid_private_key=settings.VAPID_PRIVATE_KEY,
                vapid_claims={"sub": "mailto:you@example.com"}
            )
        except Exception as e:
            print("Failed to send push:", e)
