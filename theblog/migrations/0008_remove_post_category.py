# Generated by Django 4.2.7 on 2023-11-14 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_delete_category_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
