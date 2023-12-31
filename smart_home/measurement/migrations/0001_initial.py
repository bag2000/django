# Generated by Django 4.2.5 on 2023-09-26 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Температура')),
                ('date_of', models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor')),
            ],
        ),
    ]
