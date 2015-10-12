# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('instrucciones', models.TextField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
