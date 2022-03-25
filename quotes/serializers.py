from rest_framework import serializers
from helpers.serializers import DateTimeFieldWihTZ
from quotes.models import Quote,QuoteRequest


class QuoteRequestSerializer(serializers.ModelSerializer):
    request_timestamp = DateTimeFieldWihTZ(format="%d/%m/%Y %H:%M")
    event_date = DateTimeFieldWihTZ(format="%d/%m/%Y %H:%M")
    client = serializers.StringRelatedField()

    class Meta:
        model = QuoteRequest
        fields = ('request_timestamp','event_date','event_name','client','get_create_quote_url','get_detail_url')

class QuoteSerializer(serializers.ModelSerializer):
    evaluation_date = DateTimeFieldWihTZ(format="%d/%m/%Y %H:%M")
    quote_request = serializers.StringRelatedField()

    class Meta:
        model = Quote
        fields = ('quote_request','evaluation_date','proposal_value','note','get_detail_url')
