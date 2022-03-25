from django import forms
from quotes.models import Quote, QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    """Form definition for QuoteRequest."""

    class Meta:
        """Meta definition for QuoteRequestform."""

        model = QuoteRequest
        fields = ('event_date','event_name','note')
        

class QuoteForm(forms.ModelForm):
    """Form definition for Quote."""

    class Meta:
        """Meta definition for Quoteform."""

        model = Quote
        fields = ('proposal_value','note')
