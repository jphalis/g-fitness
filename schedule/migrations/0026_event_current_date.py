# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0025_auto_20150319_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='current_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 22, 3, 2, 659006, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
