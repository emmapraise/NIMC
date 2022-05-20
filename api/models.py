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


class common(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Admin(common):
    ADMIN_TYPE = (
        ("Local", "Local Goverment"),
        ("State", "State Goverment"),
        ("Federal", "Federal Goverment"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    admin_type = models.CharField(
        max_length=10, choices=ADMIN_TYPE, null=True, blank=True
    )

    def __str__(self):
        return self.user
