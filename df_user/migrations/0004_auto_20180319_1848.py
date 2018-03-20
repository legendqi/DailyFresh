# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0003_auto_20180318_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='receiveInformation',
        ),
        migrations.AddField(
            model_name='receiveinfo',
            name='userinfo',
            field=models.ForeignKey(to='df_user.UserInfo', default=1),
        ),
    ]
