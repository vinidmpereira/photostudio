# Generated by Django 2.0 on 2018-08-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_contract_local'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Contrato', 'verbose_name_plural': 'Contratos'},
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_file',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='contracts/', verbose_name='Contrato Digitalizado'),
        ),
    ]
