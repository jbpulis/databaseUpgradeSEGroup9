# Generated by Django 2.1.2 on 2018-11-03 19:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_auto_20181029_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='dateAdded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
