# Generated by Django 4.2.6 on 2023-10-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_alter_trip_important_files_alter_trip_trip_pictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='on_wishlist',
            field=models.BooleanField(default=False),
        ),
    ]
