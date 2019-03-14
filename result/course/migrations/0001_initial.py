# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-07 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marks', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(related_name='subjects', to='course.Subject'),
        ),
    ]
