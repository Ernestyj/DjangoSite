# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

# Create your models here.

User = get_user_model()


class UserFav(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品", help_text="商品id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __unicode__(self):
        return self.user.username


class UserLeavingMessage(models.Model):
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(User, verbose_name="User")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="Message type",
                                       help_text=u"留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)")
    subject = models.CharField(max_length=100, default="", verbose_name="Subject")
    message = models.TextField(default="", verbose_name="Message", help_text="Message")
    file = models.FileField(upload_to="message/images/", verbose_name="Upload file", help_text="Upload file")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name = "User message"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.subject


class UserAddress(models.Model):
    user = models.ForeignKey(User, verbose_name="User")
    province = models.CharField(max_length=100, default="", verbose_name="Province")
    city = models.CharField(max_length=100, default="", verbose_name="City")
    district = models.CharField(max_length=100, default="", verbose_name="District")
    address = models.CharField(max_length=100, default="", verbose_name="Address")
    signer_name = models.CharField(max_length=100, default="", verbose_name="Signer")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="Mobile")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name = "Shipping address"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.address