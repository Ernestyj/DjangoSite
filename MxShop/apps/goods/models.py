# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.

class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1, "First category"),
        (2, "Second category"),
        (3, "Third category"),
    )

    parent_category = models.ForeignKey('self', null=True, verbose_name='Parent category', blank=True, help_text='Parent category',
                                        related_name='sub_cat')
    name = models.CharField(default='', max_length=30, verbose_name='Category name', help_text='Category name')
    code = models.CharField(default='', max_length=30, verbose_name='Category code', help_text='Category code')
    desc = models.TextField(default="", verbose_name="Category description", help_text="Category description")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="Category type", help_text="Category type")
    is_tab = models.BooleanField(default=False, verbose_name="Is navigation", help_text="Is navigation")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='Add time')

    class Meta:
        verbose_name = 'Goods category'
        verbose_name_plural = 'Goods categories'


class GoodsCategoryBrand(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="Goods category")
    name = models.CharField(default="", max_length=30, verbose_name="Brand name", help_text="Brand name")
    desc = models.TextField(default="", max_length=200, verbose_name="Brand description", help_text="Brand description")
    image = models.ImageField(max_length=200, upload_to='brands/')
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='Add time')

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = 'Brands'
        db_table = "goods_goodsbrand"

    def __unicode__(self):
        return self.name


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory, verbose_name="Goods category")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="Goods UID")
    name = models.CharField(max_length=100, verbose_name="Goods name")
    click_num = models.IntegerField(default=0, verbose_name="Click number")
    sold_num = models.IntegerField(default=0, verbose_name="Sold number")
    fav_num = models.IntegerField(default=0, verbose_name="Favorite number")
    goods_num = models.IntegerField(default=0, verbose_name="Goods number")
    market_price = models.FloatField(default=0, verbose_name="Market price")
    shop_price = models.FloatField(default=0, verbose_name="SHop price")
    goods_brief = models.TextField(max_length=500, verbose_name="Goods brief")
    goods_desc = UEditorField(verbose_name="Goods description", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=True, verbose_name="Is ship free")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="Front image")
    is_new = models.BooleanField(default=False, verbose_name="Is new")
    is_hot = models.BooleanField(default=False, verbose_name="Is hot")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods, verbose_name="Goods image", related_name="images")
    image = models.ImageField(upload_to="", verbose_name="Image", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name = 'Goods Image'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.goods.name


class Banner(models.Model):
    goods = models.ForeignKey(Goods, verbose_name="Goods")
    image = models.ImageField(upload_to='banner', verbose_name="Banner image")
    index = models.IntegerField(default=0, verbose_name="Banner index")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name = 'Banner goods'
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.goods.name
