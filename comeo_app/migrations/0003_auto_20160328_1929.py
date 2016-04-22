# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0002_transaction_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='funding_type',
            field=models.CharField(choices=[('conditional', 'Conditional funding'), ('unconditional', 'Unconditional funding')], default='unconditional', max_length=50, verbose_name='Funding type'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='state',
            field=models.CharField(default='draft', max_length=50, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='comeouser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='comeouser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]