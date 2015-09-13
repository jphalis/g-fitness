# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_event_rule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='client_name',
            new_name='title',
        ),
    ]
