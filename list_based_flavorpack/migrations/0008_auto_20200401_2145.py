# Generated by Django 3.0.2 on 2020-04-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_based_flavorpack', '0007_auto_20191219_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listbasedregion',
            name='processing_class_path',
            field=models.CharField(default='list_based_flavorpack.processing_classes.third_party_processing.processing.DBProcessingClass', help_text='The full python path to the class that will be processing region allocations', max_length=150, verbose_name='Processing Class Path'),
        ),
    ]
