# Generated by Django 2.0.7 on 2018-08-10 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'verbose_name': 'Proposta', 'verbose_name_plural': 'Propostas'},
        ),
    ]