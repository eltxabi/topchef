# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_auto_20151019_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
