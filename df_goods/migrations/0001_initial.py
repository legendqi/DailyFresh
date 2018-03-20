# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gImage', models.ImageField(upload_to='df_goods')),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(max_length=20)),
                ('gclick', models.IntegerField()),
                ('gdescriptioni', models.CharField(max_length=200)),
                ('gstore', models.IntegerField()),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='df_goods.GoodsType'),
        ),
    ]
