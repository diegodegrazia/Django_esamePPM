# Generated by Django 4.2.11 on 2024-06-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_post_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
