# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-07 08:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0019_auto_20170508_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='elibrary',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 8, 39, 1, 465014), verbose_name='Отправка журнала в Elibrary'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='priem',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 8, 39, 10, 439523), verbose_name='Прием статей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='publish',
            field=models.DateField(default=datetime.datetime(2018, 4, 7, 8, 39, 15, 187277), verbose_name='Размещение журнала в электронном виде'),
            preserve_default=False,
        ),
    ]