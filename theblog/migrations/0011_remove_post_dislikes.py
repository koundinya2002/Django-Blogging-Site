# Generated by Django 4.2.5 on 2023-11-17 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_post_dislikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
    ]
