# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0018_auto_20150318_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(related_name='creator', default=1, verbose_name='client', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
