# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapp', '0007_det'),
    ]

    operations = [
        migrations.DeleteModel(
            name='det',
        ),
    ]
