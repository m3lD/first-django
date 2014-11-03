# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True, help_text='Uri identifier.')),
                ('content_markdown', models.TextField(verbose_name='Content (Markdown)')),
                ('content_markup', models.TextField(verbose_name='Content (Markup)')),
                ('date_publish', models.DateTimeField(verbose_name='Publish Date')),
            ],
            options={
                'verbose_name': 'Article',
                'ordering': ['-date_publish'],
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True, help_text='Uri identifier.')),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['title'],
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(verbose_name='Categories', null=True, to='blog.Category', blank=True),
            preserve_default=True,
        ),
    ]
