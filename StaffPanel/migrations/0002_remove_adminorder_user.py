# Generated by Django 3.2.9 on 2022-01-11 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StaffPanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminorder',
            name='user',
        ),
    ]
