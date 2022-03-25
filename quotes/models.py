from django.db import models
from django.urls import reverse
from clients.models import Client


# Create your models here.

class QuoteRequest(models.Model):
    """Model definition for BudgetRequest."""

    request_timestamp = models.DateTimeField(verbose_name='Data Requisição', auto_now=False, auto_now_add=True)
    event_date = models.DateTimeField(verbose_name='Data/Hora do evento', auto_now=False, auto_now_add=False)
    event_name = models.CharField(verbose_name='Nome do Evento', max_length=180)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_budget_request')
    note = models.TextField(verbose_name='Observação')

    def get_detail_url(self):
        
        return reverse('detail_quote_request', kwargs={'pk':self.pk})

    def get_create_quote_url(self):

        return reverse('create_quote', kwargs={'quote_request':self.pk})

    class Meta:
        """Meta definition for BudgetRequest."""

        verbose_name = 'Solicitação de Orçamento'
        verbose_name_plural = 'Solicitações de Orçamento'

    def __str__(self):
        """Unicode representation of BudgetRequest."""
        return '%s - %s' % (self.event_date,self.event_name)

class Quote(models.Model):
    """Model definition for Budget."""

    quote_request = models.ForeignKey(QuoteRequest, on_delete=models.CASCADE)
    evaluation_date = models.DateTimeField(verbose_name='Data de avaliação', auto_now=False, auto_now_add=True)
    proposal_value = models.FloatField(verbose_name='Valor da Proposta')
    note = models.TextField(verbose_name='Observação')

    
    def get_detail_url(self):
        
        return reverse('detail_quote', kwargs={'pk':self.pk})

    def get_create_complete_contract_url(self):

        return reverse('create_complete_contract', kwargs={'client':self.quote_request.client.pk, 'quote':self.pk})

    class Meta:
        """Meta definition for Budget."""

        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'

    def __str__(self):
        """Unicode representation of Budget."""
        return '%s - %s' % (self.quote_request, self.evaluation_date)
