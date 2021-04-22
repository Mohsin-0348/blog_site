from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
from .choices import UserChoices
from .manager import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=60,
        unique=True,
    )
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)  # a superuser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=10, choices=UserChoices.choices, default=UserChoices.USER)
    contact = models.PositiveIntegerField(blank=True, null=True)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Email & Password are required by default.

    objects = UserManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.username + ' ' + self.email
        
    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        return "username: " + self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
