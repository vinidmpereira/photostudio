"""clients URL Configuration

"""
from django.urls import path
from contracts.views import contract_index,create_client_contract, create_complete_contract, ContractDetailView, ContractDeleteView, ContractUpdateView, contract_results_panel,event_anniversarys

urlpatterns = [
    path('',contract_index, name='contract_index'),
    path('create/<int:client>', create_client_contract, name='create_client_contract'),
    path('create/<int:client>/<int:quote>', create_complete_contract, name='create_complete_contract'),
    path('<int:pk>/detail', ContractDetailView.as_view(), name='detail_contract'),
    path('<int:pk>/update', ContractUpdateView.as_view(), name='update_contract'),
    path('<int:pk>/delete', ContractDeleteView.as_view(), name='delete_contract'),
    path('results_panel/', contract_results_panel, name='results_panel'),
    path('event_anniversarys/', event_anniversarys, name='event_anniversarys'),
]