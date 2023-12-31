# Generated by Django 2.1.1 on 2018-09-27 17:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('serialbox', '0001_initial'),
        ('quartet_output', '0002_auto_20180909_0946'),
        ('quartet_capture', '0001_initial'),
        ('quartet_templates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListBasedRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The date and time that this record was created', verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, help_text='The date and time that this record was modified last.', verbose_name='Last Modified')),
                ('readable_name', models.CharField(help_text='A human-readable name for use in GUIs and reports and such.', max_length=100, unique=True, verbose_name='Readable Name')),
                ('machine_name', models.CharField(help_text='A url/api-friendly unique key for use in API calls and such.', max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Only numbers and letters are allowed. Invalid API Key.')], verbose_name='API Key')),
                ('active', models.BooleanField(default=True, help_text='Whether or not this pool is active/in-use. If marked false the pool will no longer be able to be used in API calls, etc.', verbose_name='Active')),
                ('order', models.IntegerField(blank=True, help_text='The order in which this region will be consumed as numbers are issued from the pool overall', null=True, verbose_name='Order')),
                ('last_number_line', models.IntegerField(default=1, help_text='The line number of the last number issued maintains the state of the list-based region.', verbose_name='Last Number Line')),
                ('processing_class_path', models.CharField(help_text='The full python path to the class that will be processing region allocations', max_length=150, verbose_name='Processing Class Path')),
                ('file_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('directory_path', models.CharField(blank=True, default='/var/quartet/numbers', help_text='The full path to the directory where numbers will be stored. Leave blank for default. Default is /var/quartet/numbers', max_length=150, null=True)),
                ('number_replenishment_size', models.IntegerField(help_text='The size that the outbound message will request from the third-party system, if numbers available are low. E.g.: 500', verbose_name='Number Replenishment Size')),
                ('authentication_info', models.ForeignKey(help_text='The Authentication Info to use.', null=True, on_delete=django.db.models.deletion.PROTECT, to='quartet_output.AuthenticationInfo', verbose_name='Authentication Info')),
                ('end_point', models.ForeignKey(help_text='A protocol-specific endpoint defining whereany data will come from', null=True, on_delete=django.db.models.deletion.PROTECT, to='quartet_output.EndPoint', verbose_name='End Point')),
                ('pool', models.ForeignKey(blank=True, help_text='The Number Pool this region will belong to.', null=True, on_delete=django.db.models.deletion.CASCADE, to='serialbox.Pool', verbose_name='Number Pool')),
                ('rule', models.ForeignKey(help_text='A rule that may be executed by the region processing class.', null=True, on_delete=django.db.models.deletion.PROTECT, to='quartet_capture.Rule', verbose_name='Processing Rule')),
                ('template', models.ForeignKey(help_text='The Django/Jinja template to send a formatted request for number ranges', null=True, on_delete=django.db.models.deletion.PROTECT, to='quartet_templates.Template', verbose_name='Message Template')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProcessingParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='The key part of the key-value pair. Example: q', max_length=200)),
                ('value', models.CharField(blank=True, help_text='The value part of the key-value pair.', max_length=400, null=True)),
                ('list_based_region', models.ForeignKey(help_text='A key-value pair object meant to hold parameters used for processing classes.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='processing_parameters', to='list_based_flavorpack.ListBasedRegion', verbose_name='Processing Class Parameter')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='listbasedregion',
            unique_together={('pool', 'order')},
        ),
    ]
