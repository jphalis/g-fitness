# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0012_auto_20150313_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occurrence',
            name='description',
        ),
    ]
