# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-20 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0006_photo_n_avg_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'publish'), (-1, 'delete')], default=0, help_text='状态', verbose_name='状态'),
        ),
    ]
