# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0005_receta_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='foto',
            field=models.ImageField(upload_to='media'),
        ),
    ]
