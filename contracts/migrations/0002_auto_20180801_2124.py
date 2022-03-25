# Generated by Django 2.0.7 on 2018-08-02 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='value',
            new_name='contract_value',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='responsible',
            new_name='contractant',
        ),
        migrations.AddField(
            model_name='contract',
            name='quote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_quote', to='quotes.Quote'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='quote_request',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract_request', to='quotes.QuoteRequest'),
            preserve_default=False,
        ),
    ]
