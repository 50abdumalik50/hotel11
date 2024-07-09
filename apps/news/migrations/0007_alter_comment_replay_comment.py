# Generated by Django 5.0 on 2024-07-08 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_comment_replay_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replay_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='news.comment'),
        ),
    ]