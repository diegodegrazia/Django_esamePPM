# Generated by Django 4.2.11 on 2024-06-13 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
