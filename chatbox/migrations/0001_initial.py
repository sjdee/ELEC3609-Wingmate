# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 11:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userOne', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chatroom_userOne', to=settings.AUTH_USER_MODEL)),
                ('userTwo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chatroom_userTwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name=b'content')),
                ('roomId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chatbox.Chatroom')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='chatroom',
            unique_together=set([('userOne', 'userTwo')]),
        ),
    ]
