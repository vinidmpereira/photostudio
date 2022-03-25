from django.urls import path
from quotes.views import create_quote, create_quote_request, QuoteDetailView, QuoteRequestDetailView,NeedsQREvaluation

urlpatterns = [
    path('<int:client>/create/quote_request',
         create_quote_request, name='create_quote_request'),
    path('<int:pk>/request/detail', QuoteRequestDetailView.as_view(),
         name='detail_quote_request'),
    path('<int:quote_request>/create/quote',
         create_quote, name='create_quote'),
    path('<int:pk>/detail', QuoteDetailView.as_view(), name='detail_quote'),
    path('needs_qr_evaluation', NeedsQREvaluation.as_view(), name='needs_qr_evaluation'),
]
