from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError

# ==================================Customer User Authentication Start===========================

class RegularUserTokenObtainPairView(TokenObtainPairView):
    serializer_class = RegularUserTokenObtainPairSerializer

class RegularUserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegularUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Registration Successfully!"
                }, status=status.HTTP_201_CREATED)
        
        first_error_message = serializer.errors[next(iter(serializer.errors))][0]
        return Response({
            "status": "failed",
            "message": first_error_message
        }, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response({"message": "Token is valid"}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

# ==================================Customer User Authentication End===========================


# ==================================Restaurant Authentication Start===========================

class RestaurantUserTokenObtainPairView(TokenObtainPairView):
    serializer_class = RestaurantLoginTokenObtainPairSerialier

# ==================================Restaurant Authentication End===========================



