# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 04:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='', max_length=100, verbose_name='Province')),
                ('city', models.CharField(default='', max_length=100, verbose_name='City')),
                ('district', models.CharField(default='', max_length=100, verbose_name='District')),
                ('address', models.CharField(default='', max_length=100, verbose_name='Address')),
                ('signer_name', models.CharField(default='', max_length=100, verbose_name='Signer')),
                ('signer_mobile', models.CharField(default='', max_length=11, verbose_name='Mobile')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
            ],
            options={
                'verbose_name': 'Shipping address',
                'verbose_name_plural': 'Shipping address',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6536\u85cf',
                'verbose_name_plural': '\u7528\u6237\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='UserLeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.IntegerField(choices=[(1, '\u7559\u8a00'), (2, '\u6295\u8bc9'), (3, '\u8be2\u95ee'), (4, '\u552e\u540e'), (5, '\u6c42\u8d2d')], default=1, help_text='\u7559\u8a00\u7c7b\u578b: 1(\u7559\u8a00),2(\u6295\u8bc9),3(\u8be2\u95ee),4(\u552e\u540e),5(\u6c42\u8d2d)', verbose_name='Message type')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='Subject')),
                ('message', models.TextField(default='', help_text='Message', verbose_name='Message')),
                ('file', models.FileField(help_text='Upload file', upload_to='message/images/', verbose_name='Upload file')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
            ],
            options={
                'verbose_name': 'User message',
                'verbose_name_plural': 'User message',
            },
        ),
    ]