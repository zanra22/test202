# Generated by Django 4.0.3 on 2022-09-20 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='staff',
            new_name='student',
        ),
    ]