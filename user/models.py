from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core import validators


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Pleas set email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', User.USER)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', User.ADMIN)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser staff must be true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be superuser, pleas set true")

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    USER = "user"
    ADMIN = "admin"
    ROLE = [
        (USER, "user"),
        (ADMIN, "admin"),
    ]

    email = models.EmailField(
        db_index=True,
        validators=[validators.validate_email],
        unique=True,
        blank=False,
    )
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, null=True, blank=True, verbose_name="Отчество")
    role = models.CharField(
        choices=ROLE,
        default="user",
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Роль",
    )
    date_create = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Дата создания")
    is_staff = models.BooleanField(default=False, verbose_name='Доступ к БД')
    is_active = models.BooleanField(default=False, verbose_name='Активен')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')
    post_agreement = models.BooleanField(default=False,  verbose_name='Разрешение на отправку писем')
    inn = models.CharField(max_length=12, null=True, blank=True, verbose_name="ИНН")
    bank_acaunt = models.CharField(max_length=20,  null=True, blank=True, verbose_name='Номер лицивого счета')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Адрес')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()


    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ['id',]
