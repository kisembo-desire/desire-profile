from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from Desire.managers import CustomUserManager

class CustomUser(AbstractUser):
    # userProfileImage = models.ImageField(default="<i class='fa fa-user'></i>",upload_to="userImage/")
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
