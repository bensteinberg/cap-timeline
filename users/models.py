from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from research.models import Meta


class TimelineUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email address is required')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('email_verified', True)
        kwargs.setdefault('is_active', True)
        return self.create_user(email=email, password=password, **kwargs)

    def create_staff_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('email_verified', True)
        kwargs.setdefault('is_active', True)
        return self.create_user(email=email, password=password, **kwargs)


class TimelineUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, unique=True, db_index=True,
                              verbose_name='email address',
                              error_messages={'unique': u"A user with that email address already exists.", })
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
    timelines = models.ManyToManyField(Meta, blank=True, related_name='users')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = TimelineUserManager()

    class Meta:
        verbose_name = 'User'

    def save(self, *args, **kwargs):
        if self.is_staff and not self.is_superuser:
            group = Group.objects.get(name='staff')
            self.groups.add(group)
        super(TimelineUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
