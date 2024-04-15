from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель для создания пользователей
    """

    ROLES = {
        ('user', 'пользователь'),
        ('admin', 'админ')
    }

    username = None
    first_name = models.CharField(max_length=64, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=64, verbose_name='фамилия', **NULLABLE)
    phone = models.CharField(max_length=128, verbose_name='номер телефона', **NULLABLE)
    email = models.CharField(max_length=254, unique=True, verbose_name='почта')
    role = models.CharField(max_length=150, choices=ROLES, default='user', verbose_name='роль пользователя')
    image = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} {self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
