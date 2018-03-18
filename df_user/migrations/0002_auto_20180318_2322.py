# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiveinfo',
            name='address',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='receiveinfo',
            name='phoneNumber',
            field=models.CharField(max_length=11, default=''),
        ),
        migrations.AlterField(
            model_name='receiveinfo',
            name='postalCode',
            field=models.CharField(max_length=6, default=''),
        ),
        migrations.AlterField(
            model_name='receiveinfo',
            name='username',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='receiveInformation',
            field=models.ForeignKey(to='df_user.ReceiveInfo', default=''),
        ),
    ]
