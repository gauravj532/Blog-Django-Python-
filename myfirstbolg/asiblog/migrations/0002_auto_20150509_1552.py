# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asiblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(verbose_name=b'date modified'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
