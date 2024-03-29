from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from NIMC.enums.nin import (
    bloodGroup,
    documentTypes,
    education_class_type,
    education_type,
    maritalStatus,
    genotype,
)
from NIMC.enums.admin import admin_types, approval_status
from NIMC.enums import admin


class UserManager(BaseUserManager):
    """Define a model manager for User model with email login."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """This represent the user object on the system"""

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    phone = models.CharField(max_length=11, unique=True)
    middle_name = models.CharField(max_length=25, blank=True, null=True)
    nin = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="NIMC/static/images")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    is_citizen = models.BooleanField(default=False, null=True, blank=True)
    access_code = models.CharField(default="1234", max_length=6)
    is_admin = models.BooleanField(default=False, null=True, blank=True)

    # USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()


class common(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Citizen(common):
    """This is the Model for Citizen"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class Admin(common):
    """This is the User Admin Object"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=30, choices=admin_types(), null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class NinInfoCommon(common):
    """This is model to add NIN Information of the user"""

    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    state_of_origin = models.CharField(max_length=30)
    address = models.TextField()
    marital_status = models.CharField(
        max_length=30, choices=maritalStatus(), null=True, blank=True
    )
    blood_group = models.CharField(
        max_length=10, choices=bloodGroup(), null=True, blank=True
    )
    genotype = models.CharField(max_length=2, choices=genotype(), null=True, blank=True)
    next_of_kin = models.CharField(max_length=100)
    next_of_kin_email = models.EmailField(null=True, blank=True)
    next_of_kin_phone = models.CharField(max_length=11, null=True, blank=True)
    next_of_kin_address = models.TextField()
    occupation = models.CharField(max_length=100)

    class Meta:
        abstract = True


class NinInfo(NinInfoCommon):
    """This is model to add NIN Information of the user"""

    def __str__(self):
        return f"{self.citizen.user} with NIN {self.citizen.user.nin}"


class UpdateNinInfo(NinInfoCommon):
    """This is model saves all update on Nin Info"""

    nin_info = models.ForeignKey(NinInfo, on_delete=models.CASCADE)
    document = models.FileField(
        blank=True, null=True, upload_to="NIMC/static/documents"
    )
    status = models.IntegerField(choices=approval_status(), default=admin.PENDING)

    def __str__(self):
        return f"{self.citizen.user} with NIN {self.citizen.user.nin}"


class Document(common):
    """This is the object for all uploaded document"""

    nin_info = models.ForeignKey(NinInfo, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=documentTypes())
    path = models.FileField(upload_to="NIMC/static/documents")

    def __str__(self):
        return f"{self.nin_info.citizen.user} {self.type} document"


class EducationDocument(common):
    """This is the Model to store all Educational Documents"""

    highest_education = models.CharField(max_length=100, choices=education_type())
    name_of_school = models.CharField(max_length=200, blank=True, null=True)
    year_of_graduation = models.CharField(max_length=4)
    class_of_graduation = models.CharField(
        max_length=20, choices=education_class_type()
    )
    country_of_graduation = models.CharField(max_length=20)
    certificate = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="education_certificate",
        blank=True,
        null=True,
    )
    transcript = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="education_transcript",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.highest_education


class ProfessionalDocument(common):
    """This is the model that stores all Professional Documents"""

    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year_of_achievement = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class CV(common):
    """This is the model that stores all CVs"""

    cv = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cv.document.nin_info.citizen.user} {self.type} document"


class CertificateDocument(common):
    """This is the model that stores all Certificate Documents"""

    certificate = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="certificate"
    )
    transcript = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="transcript"
    )

    def __str__(self):
        return f"Certificate Document for "


class EncodedImage(common):
    "This stores the image encoded"
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    encodings = models.TextField()

    def __str__(self):
        return self.citizen.user.get_full_name()


class Request(common):
    """This is the model that hold all the update request made"""

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

    def __str__(self):
        return f"The Request {self.title} is currently ({self.status})"
