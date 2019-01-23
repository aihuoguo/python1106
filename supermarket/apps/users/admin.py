from django.contrib import admin

# Register your models here.
from users.models import Users

admin.site.register(Users)