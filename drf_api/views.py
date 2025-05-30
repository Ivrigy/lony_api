from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
def root_route(request):
    return JsonResponse({"message": "Welcome to the API"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_route(request):
    return JsonResponse({"detail": "Logged out successfully"}, status=200)
