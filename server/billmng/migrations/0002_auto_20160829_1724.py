# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('billmng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('identifier', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('bill_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount_price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('taxes', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('power_consumed', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('user', models.ForeignKey(to='billmng.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='bills',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bills',
        ),
    ]
