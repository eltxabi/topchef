# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_auto_20151103_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='foto',
            field=models.CharField(default='foto', max_length=30),
        ),
    ]
