# Generated by Django 5.1 on 2024-09-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]