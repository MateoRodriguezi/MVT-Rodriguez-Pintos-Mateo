from django.urls import path
from familiares.views import listar_familia

urlpatterns = [
    path('', listar_familia),
]