# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_event_number_of_lessons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='number_of_lessons',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
    ]
