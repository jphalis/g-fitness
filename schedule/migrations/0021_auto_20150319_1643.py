# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0020_auto_20150319_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start'], 'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
    ]
