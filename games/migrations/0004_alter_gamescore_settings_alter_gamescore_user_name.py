# Generated by Django 5.0.2 on 2024-03-08 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_gamescore_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescore',
            name='settings',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gamescore',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
