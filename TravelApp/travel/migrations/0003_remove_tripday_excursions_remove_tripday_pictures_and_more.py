# Generated by Django 4.0.4 on 2022-04-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripday',
            name='excursions',
        ),
        migrations.RemoveField(
            model_name='tripday',
            name='pictures',
        ),
        migrations.AddField(
            model_name='tripday',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
