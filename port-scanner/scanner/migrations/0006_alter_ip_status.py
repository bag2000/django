# Generated by Django 4.2.5 on 2023-09-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0005_ip_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='status',
            field=models.CharField(choices=[('C', 'Closed'), ('O', 'Open'), ('N', 'No data')], default='No data', max_length=1),
        ),
    ]
