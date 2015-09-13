# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0016_auto_20150313_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_recurring_period',
            field=models.DateTimeField(help_text='Leave empty for one time only events.', null=True, verbose_name='end recurring period', blank=True),
            preserve_default=True,
        ),
    ]
