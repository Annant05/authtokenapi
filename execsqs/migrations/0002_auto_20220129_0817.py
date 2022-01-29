# Generated by Django 3.2.8 on 2022-01-29 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('execsqs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traceevent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traceevent',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
