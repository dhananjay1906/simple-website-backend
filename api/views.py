from django.http import JsonResponse

def get_data(request):
    return JsonResponse({"message": "Hello from Django API"})

def get_another_data(request):
    return JsonResponse({"message": "Another API Endpoint"})
