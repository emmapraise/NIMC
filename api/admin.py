from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import Admin, Citizen, Document, NinInfo, Request, User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register([Admin, NinInfo, Document, Request, Citizen])
