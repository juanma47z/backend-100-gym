# Generated by Django 5.0.6 on 2024-05-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_coach_options_alter_customer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='cell_phone',
            field=models.CharField(max_length=10, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='apellido'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cell_phone',
            field=models.CharField(max_length=10, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='apellido'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
    ]
