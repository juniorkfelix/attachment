# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=30)),
                ('job_title', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=4000)),
                ('Date', models.DateTimeField(null=True)),
                ('Rank', models.CharField(max_length=30)),
                ('Roles', models.TextField(max_length=500)),
            ],
        ),
    ]
