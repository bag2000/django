# Generated by Django 4.2.5 on 2023-09-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0004_remove_company_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='status',
            field=models.CharField(choices=[('C', 'Closed'), ('O', 'Open'), ('N', 'No data')], default='N', max_length=1),
        ),
    ]
