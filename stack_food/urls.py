from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('custom_user.urls')),
    path('admin-staff/', include('admin_staff.urls')),
    path('customer/', include('customer.urls')),
    path('driver/', include('driver.urls')),
    path('restaurant/', include('restaurant.urls')),
]
