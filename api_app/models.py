from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser, PermissionsMixin,BaseUserManager)


# Custom user manager profile
class UserProfileManager(BaseUserManager):
    """
    This class is used for alters the default settings of Django's account
    management to change from using username/password to email/password
    """

    def create_user(self, email, name, password=None):
        """
        Creates and saves a user with the given email and
        password.
        """
        # must provide email address
        if not email:
            raise ValueError('User must have an email address')
        # normalize email address by lowercasing the domain portion
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with a given password
        """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

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
