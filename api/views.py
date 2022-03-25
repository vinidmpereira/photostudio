from django.shortcuts import render
from django.db.models import Exists, OuterRef, Sum
from django.forms.fields import DateTimeField
from django.utils import timezone
from django.db.models.functions import TruncMonth, TruncYear
from clients.models import Client
from clients.serializers import ClientSerializer
from quotes.models import Quote, QuoteRequest
from quotes.serializers import QuoteSerializer, QuoteRequestSerializer
from contracts.models import Contract, Type
from contracts.serializers import ContractSerializer, ContractTotalsSerializer, ContractTotalsByTypeSerializer, YearSerializer
# Create your views here.
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated


# TODO: Cria view de api para retornar qr que precisam de atenção

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def get_clients(request):
    clients = Client.objects.all()

    if request.method == 'GET':
        name = request.GET.get('name', '')
        cpf = request.GET.get('cpf', '')

        if name:
            clients = clients.filter(name__icontains=name)
        if cpf:
            clients = clients.filter(cpf__icontains=cpf)

        return Response(ClientSerializer(clients, many=True).data)

    return Response(ClientSerializer(clients, many=True).data)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def get_quote_requests(request):
    quotes = QuoteRequest.objects.all()

    if request.is_ajax():
        client = request.GET.get('client')

        if client:
            quotes = quotes.filter(client=int(client))

    return Response(QuoteRequestSerializer(quotes, many=True).data)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def get_quotes(request):
    quotes = Quote.objects.all()

    if request.is_ajax():
        quote_request = request.GET.get('quote_request')

        if quote_request:
            quotes = quotes.filter(quote_request=int(quote_request))

    return Response(QuoteSerializer(quotes, many=True).data)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def get_contracts(request):
    contracts = Contract.objects.all().order_by('-event_date')

    if request.is_ajax():
        client = request.GET.get('client')
        contract_type = request.GET.get('contract_type')
        # search_date_ini = DateTimeField().to_python(request.GET.get('search_date_ini'),'')
        # search_date_end = DateTimeField().to_python(request.GET.get('search_date_end'),'')
        if client:
            contracts = contracts.filter(contractant=int(client))
        if contract_type:
            ctype = Type.objects.get(pk=int(contract_type))
            contracts = contracts.filter(event_type=ctype)
        # if search_date_ini:
        #     contracts = contracts.filter(event_date__gte=search_date_ini)
        # if search_date_end:
        #     contracts = contracts.filter(event_date__lte=search_date_end)

    return Response(ContractSerializer(contracts, many=True).data)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def quote_request_awaiting_evaluation(request):
    quote_requests = QuoteRequest.objects.annotate(
        no_quotes=~Exists(Quote.objects.filter(quote_request=OuterRef('pk'))))
    quote_requests = quote_requests.filter(no_quotes=True)

    return Response(QuoteRequestSerializer(quote_requests, many=True).data)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def get_contracts_years(request):
    year = Contract.objects.all().values('event_date__year').distinct().order_by('event_date__year')

    return Response(YearSerializer(year, many=True).data)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def get_contract_totals(request):
    contract = Contract.objects.all()
    contract_type = request.GET.get('contract_type')
    year = request.GET.get('year')

    if year:
        contract = contract.filter(event_date__year=year)
    if contract_type:
        contract_type = Type.objects.get(pk=contract_type)
        contract = contract.filter(event_type=contract_type)
        contract = contract.annotate(month=TruncMonth('event_date'),
                                        year=TruncYear('event_date')).\
            values('year', 'month','event_type__name').\
            annotate(contracts_totals=Sum('contract_value')).\
            order_by('year', 'month')

        return Response(ContractTotalsByTypeSerializer(contract, many=True).data)
    else:
        contract = contract.annotate(month=TruncMonth('event_date'),
                                    year=TruncYear('event_date')).\
            values('year', 'month',).\
            annotate(contracts_totals=Sum('contract_value')).\
            order_by('year', 'month')

        return Response(ContractTotalsSerializer(contract, many=True).data)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def get_events_anniversarys(request):
    today = timezone.now()
    
    contracts = Contract.objects.filter(event_date__month=today.month).order_by('event_date')

    return Response(ContractSerializer(contracts, many=True).data)