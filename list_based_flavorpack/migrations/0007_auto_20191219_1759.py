# Generated by Django 3.0.1 on 2019-12-19 17:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_based_flavorpack', '0006_auto_20191212_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listbasedregion',
            name='machine_name',
            field=models.CharField(help_text='A url/api-friendly unique key for use in API calls and such.', max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9\\-\\_]*$', 'Only numbers and letters are allowed. Invalid API Key.')], verbose_name='API Key'),
        ),
    ]