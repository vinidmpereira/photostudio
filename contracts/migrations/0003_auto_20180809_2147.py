# Generated by Django 2.0.7 on 2018-08-10 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_auto_20180801_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='event_schedule',
            new_name='event_hour',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='quote_request',
        ),
        migrations.AlterField(
            model_name='contract',
            name='quote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_quote', to='quotes.Quote'),
        ),
    ]
