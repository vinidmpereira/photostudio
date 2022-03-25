from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clients.forms import DataTableClientForm

@login_required
def home(request):
    form = DataTableClientForm()
    return render(request, 'home.html', {'form':form})


