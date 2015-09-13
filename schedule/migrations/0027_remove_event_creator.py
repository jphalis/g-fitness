# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0026_event_current_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='creator',
        ),
    ]
