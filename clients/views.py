from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from clients.forms import ClientForm
from clients.models import Client

# Create your views here.

# @method_decorator(login_required, name='dispatch')
class ClientCreateView(CreateView):
    
    model = Client
    form_class = ClientForm
    template_name = "./client_create.html"
    success_url = reverse_lazy('home')



class ClientDetailView(DetailView):
    model = Client
    template_name = "./client_detail.html"


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "./client_update.html"
    form_class = ClientForm
    
    def get_success_url(self):
        return reverse_lazy('detail_client',kwargs={'pk':self.kwargs['pk']})


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "./client_delete.html"
    success_url = reverse_lazy('home')
