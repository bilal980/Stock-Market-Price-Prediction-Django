# Generated by Django 3.1.2 on 2021-02-10 10:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0002_customuser_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
