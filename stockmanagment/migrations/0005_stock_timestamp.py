# Generated by Django 3.1.6 on 2021-02-06 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanagment', '0004_auto_20210206_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
