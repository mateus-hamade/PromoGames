# Generated by Django 4.1.5 on 2023-02-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_rename_main_page_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tag',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='image_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
