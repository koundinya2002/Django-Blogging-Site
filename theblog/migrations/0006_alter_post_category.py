# Generated by Django 4.2.7 on 2023-11-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Not categorized', max_length=255),
        ),
    ]
