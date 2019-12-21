from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Custom user manager profile
class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """

    def create_user(self, email, name, password=None):
        """
        Create a new user profile
        """
        # must provide email address
        if not email:
            raise ValueError('User must have an email address')
        # normalize email address

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # Encyrpt password and convert into a hash
        user.set_password(password)
        # saving resources in Django
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Create new superuser with given details
        """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        return user

# Custom user manager profile
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    User Profile Class to inherit from AbstractBaseUser and PermissionMixin
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#custom-permissions
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieve name of User
        """
        return self.name

    def get_short_name(self):
        """
        Retrieve Short Name of User
        """
        return self.name

    def __str__(self):
        """
        Return string representation of User
        """
        return self.email
