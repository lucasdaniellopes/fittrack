from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from .models import Treino, Dieta, Plano
from .serializers import TreinoSerializer, DietaSerializer, PlanoSerializer

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.filter(deleted_at__isnull=True)
    serializer_class = TreinoSerializer

class DietaViewSet(viewsets.ModelViewSet):
    queryset = Dieta.objects.filter(deleted_at__isnull=True)
    serializer_class = DietaSerializer

class PlanoViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.filter(deleted_at__isnull=True)
    serializer_class = PlanoSerializer