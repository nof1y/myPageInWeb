# Generated by Django 4.2.4 on 2023-08-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_advertisements_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(null=True, upload_to='djangoPage/', verbose_name='Изображение'),
        ),
    ]
