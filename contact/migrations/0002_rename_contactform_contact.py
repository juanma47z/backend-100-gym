# Generated by Django 5.0.6 on 2024-05-27 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='Contact',
        ),
    ]