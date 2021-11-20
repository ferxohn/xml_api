import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        """Create and saves a new user"""
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Creates and saves a new super user"""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'


class Client(models.Model):
    """RFC y razón social"""
    rfc = models.CharField(max_length=255, unique=True)
    razon_social = models.CharField(max_length=255, unique=True)


class CFDI(models.Model):
    """CFDI object"""
    fecha = models.DateTimeField()
    uuid = models.CharField(max_length=36)
    serie = models.CharField(max_length=255)
    folio = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=255)
    lugar_expedicion = models.CharField(max_length=5)
    metodo_pago = models.CharField(max_length=3)
    tipo_comprobante = models.CharField(max_length=1)
    moneda = models.CharField(max_length=3)
    total = models.DecimalField(max_digits=13, decimal_places=2)
    subtotal = models.DecimalField(max_digits=13, decimal_places=2)
    forma_pago = models.CharField(max_length=2)
    xml_path = models.FileField(upload_to='uploads/%Y/%m/%d/')
    
    def _str_(self):
        return self.uuid

class CFDIIssued(CFDI):
    RFC_emisor = models.CharField(max_length=13)
    razon_social_emisor = models.CharField(max_length=255)
    RFC_receptor = models.CharField(max_length=13)
    razon_social_receptor = models.CharField(max_length=255)
    #user = models.ForeignKey('User', on_delete=models.CASCADE)
    #client = models.ForeignKey('Client', on_delete = models.CASCADE)

class CFDIReceived(CFDI):
    RFC_emisor = models.CharField(max_length=13)
    razon_social_emisor = models.CharField(max_length=255)
    RFC_receptor = models.CharField(max_length=13)
    razon_social_receptor = models.CharField(max_length=255)
    #client = models.ForeignKey('Client', on_delete = models.CASCADE)
