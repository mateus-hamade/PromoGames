# Generated by Django 4.1.5 on 2023-02-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_rename_publisher_game_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]