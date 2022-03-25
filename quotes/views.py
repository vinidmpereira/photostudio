from django.shortcuts import render, redirect
from django.urls import reverse
from quotes.models import Quote, QuoteRequest
from clients.models import Client
from quotes.forms import QuoteRequestForm, QuoteForm
from django.views.generic import DetailView, TemplateView




class NeedsQREvaluation(TemplateView):
    template_name = "./quote_request_evaluation.html"



def create_quote_request(request, client):
    client = Client.objects.get(pk=client)

    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote_request = form.save(commit=False)
            quote_request.client = client
            quote_request.save()
            return redirect('home')
    else:
        
        form = QuoteRequestForm()

    return render(request, './create_quote_request.html', {'form': form})


class QuoteRequestDetailView(DetailView):
    model = QuoteRequest
    template_name = "./detail_quote_request.html"


def create_quote(request, quote_request):
    qr = QuoteRequest.objects.get(pk=quote_request)
    

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.quote_request = qr
            quote.save()

            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, './create_quote.html', {'form':form,'quote_request':qr})


class QuoteDetailView(DetailView):
    model = Quote
    template_name = "./detail_quote.html"
