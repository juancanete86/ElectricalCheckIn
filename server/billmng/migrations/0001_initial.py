# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('identifier', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('bill_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount_price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('taxes', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('power_consumed', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_card', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.AddField(
            model_name='bills',
            name='user',
            field=models.ForeignKey(to='billmng.User'),
        ),
    ]
