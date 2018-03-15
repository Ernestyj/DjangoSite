# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Name')
    birthday = models.DateField(null=True, blank=True, verbose_name='Birthday')
    gender = models.CharField(max_length=6, choices=(('male','Male'), ('female', 'Female')), default='male', verbose_name='Gender')
    mobile = models.CharField(max_length=11, verbose_name='Mobile', null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        # can not return self.name, or will get None error
        return self.username


class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name='Verify code')
    mobile = models.CharField(max_length=11, verbose_name='Mobile')
    add_time = models.DateField(default=datetime.now(), verbose_name='Add time')

    class Meta:
        verbose_name = 'Verify code'
        verbose_name_plural = 'Verify codes'

    def __unicode__(self):
        return self.code
