from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractUser

from NIMC.enums.nin import document_types
from NIMC.enums.admin import admin_types, approval_status
from NIMC.enums import admin, nin


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

    # USERNAME_FIELD = "nin"

    def __str__(self):
        return self.get_full_name()


class common(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Admin(common):
    """This is the User Admin Object"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=30, choices=admin_types(), null=True, blank=True)

    def __str__(self):
        return self.user


class NinInfo(common):
    """This is model to add NIN Information of the user"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_brith = models.DateField()
    state_of_origin = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    address = models.TextField()
    next_of_kin = models.CharField(max_length=100)
    next_of_kin_address = models.TextField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.user}) NIN information"


class Document(common):
    """This is the object for all uploaded document"""

    nin_info = models.ForeignKey(NinInfo, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=document_types())
    path = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.type


class Request(common):
    """This is the model that hold all the request made"""

    title = models.CharField(max_length=100)
    description = models.TextField()
    field = models.CharField(max_length=100)
    old_value = models.CharField(max_length=250)
    new_value = models.CharField(max_length=250)
    nin_info = models.ForeignKey(NinInfo, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(
        Admin, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    document_path = models.FileField(upload_to="documents/")
    status = models.IntegerField(choices=approval_status(), default=admin.PENDING)

    def __str__(self):
        return f"The Request {self.title} is currently ({self.status})"
