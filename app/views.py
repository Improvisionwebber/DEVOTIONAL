from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
from django.http import JsonResponse
from .models import Subscriber
import json

def subscribe_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get('email')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        # Save to database
        try:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                message = "Subscribed successfully!"
            else:
                message = "You are already subscribed!"
            return JsonResponse({'message': message})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import PushSubscription

@csrf_exempt
def save_subscription(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Save subscription to DB
        PushSubscription.objects.create(subscription=json.dumps(data))
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)

