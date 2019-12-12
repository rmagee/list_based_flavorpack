# Generated by Django 2.1.2 on 2019-12-12 17:55

from django.db import migrations, models
import list_based_flavorpack.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('list_based_flavorpack', '0005_auto_20191106_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='listbasedregion',
            name='database_name',
            field=models.CharField(blank=True, default=list_based_flavorpack.models.haikunate, help_text='The name of the database file if this is a database range.', max_length=50, null=True, verbose_name='Database File'),
        ),
        migrations.AlterField(
            model_name='listbasedregion',
            name='file_id',
            field=models.UUIDField(default=uuid.uuid1, help_text='If this range utilizes list-based files, then this willbe the name of the file located in the directory path.', verbose_name='File Name'),
        ),
    ]