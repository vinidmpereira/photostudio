from rest_framework import serializers
from contracts.models import Contract
from helpers.serializers import DateTimeFieldWihTZ


class ContractSerializer(serializers.ModelSerializer):
    event_date = DateTimeFieldWihTZ(format="%d/%m/%Y %H:%M")
    event_type = serializers.StringRelatedField()
    contractant = serializers.StringRelatedField()

    class Meta:
        model = Contract
        fields = ('event_date', 'event_name', 'event_type',
                  'contractant', 'contract_value', 'get_detail_url')


class YearSerializer(serializers.Serializer):
    event_date__year = serializers.CharField()


class ContractTotalsSerializer(serializers.Serializer):

    month = DateTimeFieldWihTZ(format="%m")
    year = DateTimeFieldWihTZ(format="%Y")
    contracts_totals = serializers.FloatField()

class ContractTotalsByTypeSerializer(serializers.Serializer):

    month = DateTimeFieldWihTZ(format="%m")
    year = DateTimeFieldWihTZ(format="%Y")
    event_type__name = serializers.CharField()
    contracts_totals = serializers.FloatField()