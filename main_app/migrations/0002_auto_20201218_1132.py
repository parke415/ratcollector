# Generated by Django 3.1.4 on 2020-12-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rat',
            name='sex',
            field=models.CharField(max_length=100),
        ),
    ]