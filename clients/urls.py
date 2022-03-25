from django.urls import path
from clients.views import ClientCreateView, ClientDetailView,ClientDeleteView, ClientUpdateView

urlpatterns = [
    path('create', ClientCreateView.as_view(), name='create_client'),
    path('<int:pk>/detail', ClientDetailView.as_view(), name='detail_client'),
    path('<int:pk>/update', ClientUpdateView.as_view(), name='update_client'),
    path('<int:pk>/delete', ClientDeleteView.as_view(), name='delete_client'),
]
