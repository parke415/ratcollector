# Generated by Django 3.1.4 on 2021-01-04 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201223_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rat',
            name='outfits',
        ),
        migrations.AddField(
            model_name='outfit',
            name='rat',
            field=models.ManyToManyField(to='main_app.Rat'),
        ),
    ]
