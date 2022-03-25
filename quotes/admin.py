from django.contrib import admin
from quotes.models import Quote, QuoteRequest
# Register your models here.

admin.site.register(Quote)
admin.site.register(QuoteRequest)