from django.db import models
from django.urls import reverse

from clients.models import Client
from quotes.models import Quote, QuoteRequest

# Create your models here.


class Type(models.Model):
    """Model definition for Type."""
    name = models.CharField(verbose_name='Tipo Contrato', max_length=50)

    class Meta:
        """Meta definition for Type."""

        verbose_name = 'Tipo contrato'
        verbose_name_plural = 'Tipos de contrato'

    def __str__(self):
        """Unicode representation of Type."""
        return self.name


class Contract(models.Model):
    """Model definition for Contract."""

    event_date = models.DateTimeField(
        verbose_name='Data/Hora do Evento', auto_now=False, auto_now_add=False)
    event_name = models.CharField(verbose_name='Nome do Evento', max_length=50)
    event_type = models.ForeignKey(
        Type, on_delete=models.PROTECT, verbose_name='Tipo de Evento')
    local = models.CharField(verbose_name='Local',
                             max_length=150, null=True, blank=True)
    contractant = models.ForeignKey(Client, on_delete=models.PROTECT)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE,
                              related_name='contract_quote', null=True, blank=True)
    contract_value = models.FloatField(verbose_name='Valor do contrato')
    note = models.TextField(verbose_name='Observações')
    contract_file = models.FileField(
        verbose_name='Contrato Digitalizado', upload_to='contracts/', max_length=250, null=True, blank=True)

    def get_detail_url(self):

        return reverse('detail_contract', kwargs={'pk': self.pk})

    def get_update_url(self):

        return reverse('update_contract', kwargs={'pk': self.pk})

    def get_delete_url(self):

        return reverse('delete_contract', kwargs={'pk': self.pk})

    def contract_file_exists(self):
        return self.contract_file != ''

    class Meta:
        """Meta definition for Contract."""

        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        """Unicode representation of Contract."""
        return '%s - %s' % (self.event_date, self.event_name)
