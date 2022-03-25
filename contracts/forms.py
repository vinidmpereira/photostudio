from django import forms
from contracts.models import Contract, Type



# for contract in Contract.objects.all().values('event_date__year').distinct().order_by('event_date__year'):


class EmptyChoiceField(forms.ChoiceField):
    def __init__(self, choices=(), empty_label=None, required=True, widget=None, label=None,
                 initial=None, help_text=None, *args, **kwargs):

        # prepend an empty label if it exists (and field is not required!)
        if not required and empty_label is not None:
            choices = tuple([(u'', empty_label)] + list(choices))

        super(EmptyChoiceField, self).__init__(choices=choices, required=required, widget=widget, label=label,
                                               initial=initial, help_text=help_text, *args, **kwargs)


class ContractForm(forms.ModelForm):
    """Form definition for Contract."""

    class Meta:
        """Meta definition for Contractform."""

        model = Contract
        fields = ('event_date', 'local', 'event_name', 'event_type',
                  'contract_value', 'note', 'contract_file')
        widgets = {
            'event_type': forms.Select(attrs={'class': 'ui fluid dropdown'}),
        }


class DataTableContractForm(forms.Form):
    """AjClientForm definition."""

    client = forms.CharField(label='Cliente', max_length=50, required=False)


class DTContratTypeForm(forms.Form):
    """DTContratTypeForm definition."""

    contract_type = forms.ModelChoiceField(label='Tipo', queryset=Type.objects.all(
    ), widget=forms.Select(attrs={'class': 'ui fluid dropdown'}))
    search_date_ini = forms.DateField(label='Data Início')
    search_date_end = forms.DateField(label='Data Fim')


class ResultPanelForm(forms.Form):
    """DTContratTypeForm definition."""

    contract_type = forms.ModelChoiceField(label='Tipo', queryset=Type.objects.all(
    ), widget=forms.Select(attrs={'class': 'ui fluid dropdown'}))
    year = EmptyChoiceField(label='Ano', empty_label='-----------', choices=[],
                            widget=forms.Select(attrs={'class': 'ui fluid dropdown'}))

