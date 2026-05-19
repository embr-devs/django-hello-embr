from django.http import HttpResponse, JsonResponse
from django.urls import path

def index(request):
    return HttpResponse("Hello from Django on Embr! 🚀")

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('', index),
    path('health', health),
    path('health/', health),
]
