# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asiblog', '0006_auto_20150513_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(to='asiblog.Post'),
        ),
    ]
