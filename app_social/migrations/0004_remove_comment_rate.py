# Generated by Django 5.1.1 on 2024-10-13 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0003_remove_comment_is_useful_remove_comment_point_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rate',
        ),
    ]
