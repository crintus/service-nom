# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-22 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('identifier', models.CharField(db_index=True, max_length=100, unique=True)),
                ('secret', models.UUIDField()),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(db_index=True, max_length=12)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('symbol', models.CharField(blank=True, max_length=30, null=True)),
                ('unit', models.CharField(blank=True, max_length=30, null=True)),
                ('divisibility', models.IntegerField(default=2)),
                ('enabled', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_nom.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('identifier', models.UUIDField()),
                ('token', models.CharField(max_length=200, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service_nom.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='company',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_company', to='service_nom.User'),
        ),
    ]