from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомизация модели User."""
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    USER_ROLE_CHOICES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )
    email = models.EmailField(max_length=254, unique=True, blank=False,)
    first_name = models.TextField(max_length=150, blank=True, null=True,)
    last_name = models.TextField(max_length=150, blank=True, null=True,)
    bio = models.TextField(blank=True, null=True,)
    role = models.CharField(
        max_length=9,
        choices=USER_ROLE_CHOICES,
    )

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
