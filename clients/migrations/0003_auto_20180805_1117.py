# Generated by Django 2.0.7 on 2018-08-05 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20180801_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.Gender', verbose_name='Genêro'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phonenumber',
            field=models.CharField(max_length=14, verbose_name='N.Telefone'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phonenumber_2',
            field=models.CharField(max_length=14, verbose_name='N.Telefone 2'),
        ),
    ]
