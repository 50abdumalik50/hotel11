# Generated by Django 5.0 on 2024-07-02 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]