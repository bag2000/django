# Generated by Django 4.2.5 on 2023-09-12 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0002_alter_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
