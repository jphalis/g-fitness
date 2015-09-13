# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20150313_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='client_name',
            field=models.CharField(default=1, max_length=100, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='end_recurring_period',
            field=models.DateTimeField(help_text='Leave empty for one time only events.', null=True, verbose_name='end recurring period', blank=True),
            preserve_default=True,
        ),
    ]
