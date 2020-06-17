from commons.models import CustomBaseModel
from django.contrib.auth.models import AbstractUser


class User(CustomBaseModel, AbstractUser):
    pass
    