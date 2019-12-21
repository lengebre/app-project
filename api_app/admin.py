from django.contrib import admin

from api_app import models

# Register your models here. This makes the admin portal available

admin.site.register(models.UserProfile)
