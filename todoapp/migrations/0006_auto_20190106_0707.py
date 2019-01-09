# Generated by Django 2.0.9 on 2019-01-06 07:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20190105_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='link_code',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]