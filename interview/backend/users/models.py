from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin
)

from .signals import create_cart_for_new_user


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(verbose_name='name', max_length=30, blank=True)
    username = models.CharField(verbose_name='username', max_length=30,
                                blank=True, unique=True,
                                )
    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False, )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True, )

    date_joined = models.DateTimeField(
        verbose_name='date joined', default=timezone.now)

    created = models.BooleanField(
        verbose_name='created',
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', ]


post_save.connect(create_cart_for_new_user, sender=User)
