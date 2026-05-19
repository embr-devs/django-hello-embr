from django.http import HttpResponse, JsonResponse
from django.urls import path

def index(request):
    return HttpResponse("Hello from Django on Embr! 🚀")

def health(request):
    return JsonResponse({"status": "ok"})

def hostinfo(request):
    return JsonResponse({
        "host_header": request.META.get("HTTP_HOST"),
        "get_host": request.get_host(),
        "x_forwarded_host": request.META.get("HTTP_X_FORWARDED_HOST"),
        "x_forwarded_proto": request.META.get("HTTP_X_FORWARDED_PROTO"),
        "x_forwarded_for": request.META.get("HTTP_X_FORWARDED_FOR"),
        "server_name": request.META.get("SERVER_NAME"),
        "all_headers": {k: v for k, v in request.META.items() if k.startswith("HTTP_")},
    })

urlpatterns = [
    path('', index),
    path('health', health),
    path('health/', health),
    path('hostinfo', hostinfo),
]
