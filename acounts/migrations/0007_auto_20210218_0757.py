# Generated by Django 3.1.2 on 2021-02-18 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0006_auto_20210212_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]
