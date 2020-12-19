# Generated by Django 3.1.4 on 2020-12-19 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201218_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='outing date')),
                ('round', models.CharField(choices=[('M', 'Morning'), ('N', 'Noon'), ('E', 'Evening')], default='M', max_length=1)),
                ('rat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.rat')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
