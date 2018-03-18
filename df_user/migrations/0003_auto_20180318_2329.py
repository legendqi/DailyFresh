# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_auto_20180318_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='receiveInformation',
            field=models.ForeignKey(to='df_user.ReceiveInfo'),
        ),
    ]
