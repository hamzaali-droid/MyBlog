# Generated by Django 4.1.5 on 2023-01-14 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_post_desc_post_post_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_desc',
        ),
    ]
