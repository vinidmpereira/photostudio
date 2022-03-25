from rest_framework import serializers
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format="%d/%m/%Y")

    class Meta:
        model = Client
        fields = ('name', 'cpf', 'rg', 'phonenumber', 'phonenumber_2',
                  'email', 'birthday', 'get_detail_url', 'quote_request_create_url', 'get_create_contract_url')
