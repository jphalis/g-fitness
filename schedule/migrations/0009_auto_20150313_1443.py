# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20150313_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_recurring_period',
        ),
        migrations.AlterField(
            model_name='event',
            name='client_name',
            field=models.CharField(max_length=100, verbose_name='Name of client'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(help_text='The end time must be later than the start time.', verbose_name='End'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(verbose_name='Start'),
            preserve_default=True,
        ),
    ]
