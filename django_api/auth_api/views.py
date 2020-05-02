from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token




class APIUserRegister(APIView):
    """
    Users Registration
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            data = serializer.data
            data['token'] = str(token)
            return Response(data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
