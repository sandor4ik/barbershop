# Generated by Django 4.2.2 on 2023-09-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_barberservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarberShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
