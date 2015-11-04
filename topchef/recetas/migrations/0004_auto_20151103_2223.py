# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_auto_20151020_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
