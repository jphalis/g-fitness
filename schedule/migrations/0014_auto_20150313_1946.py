# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_remove_occurrence_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='start'),
            preserve_default=True,
        ),
    ]
