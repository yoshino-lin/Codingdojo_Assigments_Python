# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-11 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_Authors_with_Templates_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(null=True, related_name='author', to='Books_Authors_with_Templates_app.Book'),
        ),
    ]
