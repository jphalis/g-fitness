# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='number_of_lessons',
            field=models.DecimalField(default=1, max_digits=100, decimal_places=1),
            preserve_default=True,
        ),
    ]
