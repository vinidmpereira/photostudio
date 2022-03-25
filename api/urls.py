"""clients URL Configuration

"""
from django.urls import path
from api.views import *

urlpatterns = [
    path('clients/', get_clients,name='get_clients'),
    path('contracts/', get_contracts,name='get_contracts'),
    path('contracts/years', get_contracts_years,name='get_contracts_years'),
    path('contracts/totals/', get_contract_totals,name='get_contract_totals'),
    path('quotes/', get_quotes,name='get_quotes'),
    path('quote_requests/', get_quote_requests,name='get_quote_requests'),
    path('quote_request_awaiting_evaluation/', quote_request_awaiting_evaluation,name='quote_request_awaiting_evaluation'),
    path('events_anniversary_today/', get_events_anniversarys, name='get_events_anniversarys'),
]
