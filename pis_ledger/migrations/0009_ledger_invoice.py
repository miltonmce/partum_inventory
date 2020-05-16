# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-08-09 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis_sales', '0010_auto_20190622_1207'),
        ('pis_ledger', '0008_ledger_dated'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ledger_invoice', to='pis_sales.SalesHistory'),
        ),
    ]