# Generated by Django 4.2.2 on 2023-09-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_barbershop_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbershop',
            name='photo',
            field=models.ImageField(null=True, upload_to='barbershop_photos/'),
        ),
    ]
