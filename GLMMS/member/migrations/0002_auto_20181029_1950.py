# Generated by Django 2.1.2 on 2018-10-30 00:50

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cell_Carriers',
            new_name='Cell_Carrier',
        ),
        migrations.RenameModel(
            old_name='Companies',
            new_name='Company',
        ),
        migrations.RenameModel(
            old_name='Organizations',
            new_name='Organization',
        ),
    ]