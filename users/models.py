from commons.models import CustomBaseModel
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.manager import UserManager


class User(CustomBaseModel, AbstractUser):
    objects = UserManager()

    username = None
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    password = models.CharField(max_length = 128)
    email = models.EmailField(unique=True,  
        max_length=128,
        #TODO: fix this NOT WORK!
        # error_messages={
        #     'unique': _("A user with that username already exists."),
        # },
    )
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    