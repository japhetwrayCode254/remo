# Generated by Django 4.2 on 2024-03-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='image',
            field=models.JSONField(default=list),
        ),
    ]