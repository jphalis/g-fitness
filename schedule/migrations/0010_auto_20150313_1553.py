# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_auto_20150313_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(help_text='The end time must be later than the start time.', verbose_name='end'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(verbose_name='start'),
            preserve_default=True,
        ),
    ]
