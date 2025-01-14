from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Regular-User', 'Regular-User'),
        ('Restaurant', 'Restaurant'),
        ('Driver', 'Driver'),
        ('Staff', 'Staff'),
    )
    email = models.EmailField(max_length=150, unique=True)
    user_type = models.CharField(max_length=25, choices=USER_TYPE_CHOICES)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.email

class NormalUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='normal_user_profile')
    full_name = models.CharField(max_length=255)
    referral_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name
    



# @receiver(post_save, sender=User)
# def create_normal_user_profile(sender, instance, created, **kwargs):
#     if created and instance.user_type == 'Regular-User':
#         NormalUser.objects.get_or_create(user=instance)


