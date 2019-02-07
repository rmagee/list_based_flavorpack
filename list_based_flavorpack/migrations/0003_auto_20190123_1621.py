# Generated by Django 2.1.5 on 2019-01-23 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_based_flavorpack', '0002_auto_20181002_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listbasedregion',
            name='authentication_info',
            field=models.ForeignKey(help_text='The Authentication Info to use.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quartet_output.AuthenticationInfo', verbose_name='Authentication Info'),
        ),
        migrations.AlterField(
            model_name='listbasedregion',
            name='end_point',
            field=models.ForeignKey(help_text='A protocol-specific endpoint defining whereany data will come from', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quartet_output.EndPoint', verbose_name='End Point'),
        ),
        migrations.AlterField(
            model_name='listbasedregion',
            name='number_replenishment_size',
            field=models.IntegerField(default=5000, help_text='The size that the outbound message will request from the third-party system, if numbers available are low. E.g.: 500', verbose_name='Number Replenishment Size'),
        ),
        migrations.AlterField(
            model_name='listbasedregion',
            name='processing_class_path',
            field=models.CharField(default='list_based_flavorpack.processing_classes.third_party_processing.processing.ThirdPartyProcessingClass', help_text='The full python path to the class that will be processing region allocations', max_length=150, verbose_name='Processing Class Path'),
        ),
        migrations.AlterField(
            model_name='listbasedregion',
            name='rule',
            field=models.ForeignKey(help_text='A rule that may be executed by the region processing class.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quartet_capture.Rule', verbose_name='Processing Rule'),
        ),
        migrations.AlterField(
            model_name='listbasedregion',
            name='template',
            field=models.ForeignKey(help_text='The Django/Jinja template to send a formatted request for number ranges', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quartet_templates.Template', verbose_name='Message Template'),
        ),
    ]