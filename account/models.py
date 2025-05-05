from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager  # Adjust the import if needed

class CustomUserModel(AbstractBaseUser, PermissionsMixin):  # ← inherit PermissionsMixin
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()  # ← this line is missing in your code
