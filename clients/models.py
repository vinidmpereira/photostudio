from django.db import models
from django.urls import reverse
# Create your models here.

class Gender(models.Model):
    """Model definition for Gender."""

    name = models.CharField(verbose_name='Nome', max_length=50)

    class Meta:
        """Meta definition for Gender."""

        verbose_name = 'Genêro'
        verbose_name_plural = 'Genêros'

    def __str__(self):
        """Unicode representation of Gender."""
        return self.name

class Client(models.Model):
    """Model definition for Client."""

    name = models.CharField(verbose_name='Nome', max_length=200)
    birthday = models.DateField(verbose_name='Data de Nascimento', auto_now=False, auto_now_add=False,blank=True,null=True)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, null=True, verbose_name='Genêro')
    cpf = models.CharField(verbose_name='CPF', max_length=14, blank=True)
    rg = models.CharField('RG', max_length=18, blank=True)
    rg_issuer = models.CharField(verbose_name='Orgão Emissor', max_length=50,blank=True)
    phonenumber = models.CharField(verbose_name='N.Telefone', max_length=14,blank=True)
    phonenumber_2 = models.CharField(verbose_name='N.Telefone 2', max_length=14,blank=True)
    address = models.CharField(verbose_name='Endereço', max_length=150,blank=True)
    address_bairro = models.CharField(verbose_name='Bairro', max_length=50,blank=True)
    postal_code = models.CharField(verbose_name='CEP', max_length=9,blank=True)
    active = models.BooleanField(verbose_name='Status', default=False)
    email = models.EmailField(verbose_name='Email', max_length=254,blank=True,null=True)

    def get_detail_url(self):
        
        return reverse('detail_client', kwargs={'pk':self.pk})

    def get_update_url(self):
        
        return reverse('update_client', kwargs={'pk':self.pk})

    def get_delete_url(self):
        
        return reverse('delete_client', kwargs={'pk':self.pk})
    
    def quote_request_create_url(self):

        return reverse('create_quote_request', kwargs={'client':self.pk})
    
    def get_create_contract_url(self):

        return reverse('create_client_contract', kwargs={'client':self.pk})
 
    class Meta:
        """Meta definition for Client."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Client."""
        return '%s' % (self.name)

