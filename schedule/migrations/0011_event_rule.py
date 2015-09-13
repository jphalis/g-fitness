# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20150313_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='rule',
            field=models.ForeignKey(blank=True, to='schedule.Rule', help_text="Select '----' for a one time only event.", null=True, verbose_name='rule'),
            preserve_default=True,
        ),
    ]
