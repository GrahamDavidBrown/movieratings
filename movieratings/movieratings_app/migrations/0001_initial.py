# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=15)),
                ('imdb_link', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings_app.Movie')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings_app.Rater')),
            ],
        ),
    ]
