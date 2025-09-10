from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from typing import Any
from .models import Passenger
from .serializers import PassengerSerializer

class PassengerListView(APIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
