from django import forms
from clients.models import Client

class ClientForm(forms.ModelForm):
    """Form definition for Client."""

    class Meta:
        """Meta definition for Clientform."""

        model = Client
        fields = ('name','birthday','gender','cpf','rg','rg_issuer','phonenumber','phonenumber_2','address','address_bairro','postal_code','email')
        widgets = {
            'gender': forms.Select(attrs={'class': 'ui fluid dropdown'}),
        }
class DataTableClientForm(forms.Form):
    """AjClientForm definition."""

    name = forms.CharField(label='Nome', max_length=50, required=False)
    cpf = forms.CharField(label='CPF', max_length=50)