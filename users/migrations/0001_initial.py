# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 05:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='sex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sex_name', models.CharField(max_length=2, null=True, verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='users_more_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='手机号码')),
                ('zhuanye', models.CharField(max_length=22, null=True, verbose_name='专业')),
                ('sex', models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to='users.sex', verbose_name='性别')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='XueLi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('xueli_name', models.CharField(max_length=6, null=True, verbose_name='学历')),
            ],
        ),
        migrations.AddField(
            model_name='users_more_info',
            name='xueli',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.XueLi', verbose_name='学历'),
        ),
    ]
