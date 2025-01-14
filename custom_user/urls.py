from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegularUserTokenObtainPairView, RegularUserRegistrationView, CustomTokenVerifyView


urlpatterns = [
    path('v1/api/user-registration/', RegularUserRegistrationView.as_view(), name='regular_user_registration'),
    path('v1/api/auth/login/', RegularUserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/api/auth/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
]
