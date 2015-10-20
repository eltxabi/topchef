# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripción', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='receta',
            name='ingredientes',
            field=models.ManyToManyField(to='recetas.Ingrediente'),
        ),
    ]
