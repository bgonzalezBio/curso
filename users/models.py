import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class BaseUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True, unique=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "BaseUser"
        verbose_name_plural = "BaseUsers"
        db_table = "base_user"


