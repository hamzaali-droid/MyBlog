# Generated by Django 4.1.5 on 2023-01-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_post_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('subscriber_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('subscriber_email', models.CharField(default='example@gmail.com', max_length=30)),
            ],
        ),
    ]