# Generated by Django 4.2.7 on 2023-11-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='CLick the above link to read the entire blog.', max_length=255),
        ),
    ]
