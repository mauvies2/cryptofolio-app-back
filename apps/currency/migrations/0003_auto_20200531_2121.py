# Generated by Django 3.0.5 on 2020-05-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_auto_20200525_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='cod',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
    ]
