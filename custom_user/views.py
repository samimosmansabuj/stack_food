from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from rest_framework import status
from .serializers import RegularUserTokenObtainPairSerializer, RegularUserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError

class RegularUserTokenObtainPairView(TokenObtainPairView):
    serializer_class = RegularUserTokenObtainPairSerializer

class RegularUserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegularUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration Successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        # serializer.is_valid(raise_exception=True)
        # return Response({"message": "Token is valid"}, status=status.HTTP_200_OK)
    
        try:
            serializer.is_valid(raise_exception=True)
            return Response({"message": "Token is valid"}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

