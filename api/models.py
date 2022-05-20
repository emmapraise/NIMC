from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """This represent the user object on the system"""

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    phone = models.CharField(max_length=11, unique=True)
    nin = models.CharField(max_length=20, unique=True)
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    USERNAME_FIELD = "nin"

    def __str__(self):
        return self.get_full_name()
