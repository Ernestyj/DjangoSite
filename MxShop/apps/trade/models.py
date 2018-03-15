# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

# Create your models here.

User = get_user_model()


class ShippingCart(models.Model):
    user = models.ForeignKey(User, verbose_name="User")
    goods = models.ForeignKey(Goods, verbose_name="Goods")
    nums = models.IntegerField(default=0, verbose_name="Number")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"Add time")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __unicode__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


class OrderInfo(models.Model):
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "success"),
        ("TRADE_CLOSED", "timeout closed"),
        ("WAIT_BUYER_PAY", "order created"),
        ("TRADE_FINISHED", "order finished"),
        ("paying", "wait to pay"),
    )

    user = models.ForeignKey(User, verbose_name="User")
    order_sn = models.CharField(unique=True, max_length=30, null=True, blank=True, verbose_name="Order number")
    trade_no = models.CharField(unique=True, max_length=100, null=True, blank=True, verbose_name=u"Trade number")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="Order status")
    post_script = models.CharField(max_length=200, verbose_name="Order comment")
    order_mount = models.FloatField(default=0.0, verbose_name="Order amount")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="Pay time")

    # User infos
    address = models.CharField(max_length=100, default="", verbose_name="Shipping address")
    signer_name = models.CharField(max_length=20, default="", verbose_name="Signer")
    singer_mobile = models.CharField(max_length=11, verbose_name="Mobile")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name = u"Order"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    order = models.ForeignKey(OrderInfo, verbose_name="Order info", related_name="goods")
    goods = models.ForeignKey(Goods, verbose_name="Goods")
    goods_num = models.IntegerField(default=0, verbose_name="Goods number")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name = "Order goods"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.order.order_sn)