# Generated by Django 5.0.2 on 2024-02-29 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescore',
            name='game',
            field=models.TextField(choices=[('MATH', 'Math Facts'), ('ANAGRAM', 'Anagram Hunt')], default='MATH'),
        ),
    ]
