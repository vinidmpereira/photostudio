from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from clients.models import Client
from contracts.forms import ContractForm, DataTableContractForm, DTContratTypeForm, ResultPanelForm
from contracts.models import Contract
from quotes.models import Quote

# Create your views here.

# TODO: Terminar os templates para contratos
# TODO: Testar os models


def contract_index(request):
    form = DTContratTypeForm()
    return render(request, './contract_home.html', {'form': form})


def create_client_contract(request, client):
    client = Client.objects.get(pk=client)

    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            client_contract = form.save(commit=False)
            client_contract.contractant = client
            if request.FILES:
                client_contract.contract_file = request.FILES['file']
            client_contract.save()
            return redirect('home')
    else:

        form = ContractForm()

    return render(request, './create_client_contract.html', {'form': form})


def create_complete_contract(request, client, quote):
    client = Client.objects.get(pk=client)
    quote = Quote.objects.get(pk=quote)
    qr = quote.quote_request

    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            client_contract = form.save(commit=False)
            client_contract.contractant = client
            if request.FILES:
                client_contract.contract_file = request.FILES['file']
                
            client_contract.quote = quote
            client_contract.save()
            return redirect('home')
    else:

        form = ContractForm(initial={'event_date': qr.event_date,
                                     'event_name': qr.event_name, 'contract_value': quote.proposal_value})

    return render(request, './create_complete_contract.html', {'form': form, 'quote_request': qr, 'quote': quote})


class ContractDetailView(DetailView):
    model = Contract
    template_name = "./detail_contract.html"


class ContractUpdateView(UpdateView):
    model = Contract
    template_name = "./update_contract.html"
    form_class = ContractForm
    success_url = reverse_lazy('home')


class ContractDeleteView(DeleteView):
    model = Contract
    template_name = "./delete_contract.html"
    success_url = reverse_lazy('home')


def contract_results_panel(request):
    form = ResultPanelForm()
    return render(request, './results_panel.html', {'form': form})

def event_anniversarys(request):
    
    return render(request, './event_anniversary_panel.html')
