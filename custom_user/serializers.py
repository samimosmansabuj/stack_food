from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import NormalUser, Restaurant

User = get_user_model()




# ==================================Customer User Authentication Start===========================

class RegularUserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs=attrs)
        user = self.user
        
        if user.user_type != "Regular-User":
            raise AuthenticationFailed("Only Regular-User type users are allowed to log in.")
        
        data['user_type'] = user.user_type
        data["email"] = user.email
        data["full_name"] = user.normal_user_profile.full_name
        return data


class RegularUserRegistrationSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    referral_code = serializers.CharField(write_only=True, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    user_type = serializers.CharField(read_only=True, required=False, default='Regular-User')
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'referral_code', 'password', 'user_type']
    
    def validate_user_type(self, value):
        if value != "Regular-User":
            raise serializers.ValidationError("Only 'Regular-User' type accounts can be created.")
        return value
    
    def create(self, validated_data):
        # validated_data['user_type'] = "Regular-User" # Ensure user_type is always set to Regular-User
        # user = User(**validated_data)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type="Regular-User" # Ensure user_type is always set to Regular-User
        )
        user.set_password(validated_data.pop('password'))
        user.save()
        
        NormalUser.objects.get_or_create(
            user=user, full_name=validated_data.pop('full_name'), referral_code=validated_data.pop('referral_code', None)
        )
        return user

# ==================================Customer User Authentication End===========================



# ==================================Restaurant Authentication Start===========================

class RestaurantLoginTokenObtainPairSerialier(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super.validate(attrs=attrs)
        user = self.user
        
        if user.user_type != "Restaurant":
            raise AuthenticationFailed("Only Restaurant type users are allowed to log in.")
        
        data["user_type"] = user.user_type
        data["email"] = user.email
        data["restaurant_name"] = user.restaurant_profile.restaurant_name
        return data


class RestaurantRegistrationSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField()
    restaurant_phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    user_type = serializers.CharField(read_only=True, required=False, default='Restaurant')
    
    class Meta:
        model = User
        fields = ['restaurant_name', 'email', 'restaurant_phone_number', 'username', 'password']
    
    def validate_user_type(self, value):
        if value != "Restaurant":
            raise serializers.ValidationError("Only 'Restaurant' type account can be created!")
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type="Restaurant"
        )
        user.set_password(validated_data.pop('password'))
        user.save()
        
        Restaurant.objects.create(
            user=user,
            restaurant_name=validated_data['restaurant_name'],
            restaurant_phone_number=validated_data['restaurant_phone_number']
        )
        return user

# ==================================Restaurant Authentication End===========================



