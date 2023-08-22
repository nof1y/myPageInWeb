# Generated by Django 4.2.4 on 2023-08-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='auction',
            field=models.BooleanField(help_text='отметьте если торг уместен', verbose_name='Торг'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterModelTable(
            name='advertisements',
            table='advertisements',
        ),
    ]
