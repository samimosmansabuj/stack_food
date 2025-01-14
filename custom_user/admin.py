from django.contrib import admin
from .models import User, NormalUser

admin.site.register(User)
admin.site.register(NormalUser)
