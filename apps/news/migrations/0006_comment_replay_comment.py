# Generated by Django 5.0 on 2024-07-03 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replay_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='news.comment'),
        ),
    ]
