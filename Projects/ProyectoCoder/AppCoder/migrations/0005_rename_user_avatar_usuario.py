# Generated by Django 4.1.4 on 2023-01-03 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='user',
            new_name='usuario',
        ),
    ]