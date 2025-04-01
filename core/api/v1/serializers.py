from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import (Treino, Dieta, TipoPlano, Cliente, HistoricoTreino, 
                        HistoricoDieta, Exercicio, Refeicao, TrocaExercicio, TrocaRefeicao, Perfil)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']
        read_only_fields = ['is_staff']

class PerfilSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    
    class Meta:
        model = Perfil
        fields = ['id', 'usuario', 'tipo', 'tipo_display', 'telefone', 'data_nascimento']

class TreinoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    
    class Meta:
        model = Treino
        fields = ['id', 'nome', 'descricao', 'duracao', 'cliente', 'cliente_nome', 'created_at', 'updated_at']

class DietaSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    
    class Meta:
        model = Dieta
        fields = ['id', 'nome', 'descricao', 'calorias', 'cliente', 'cliente_nome', 'created_at', 'updated_at']

class TipoPlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlano
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    tipo_plano_nome = serializers.CharField(source='tipo_plano.nome', read_only=True)
    perfil = PerfilSerializer(read_only=True)
    
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'data_nascimento', 'altura', 'peso', 
                 'tipo_plano', 'tipo_plano_nome', 'data_inicio_plano', 'data_fim_plano',
                 'data_ultimo_treino', 'data_ultima_dieta',
                 'trocas_exercicios_restantes', 'trocas_refeicoes_restantes', 'perfil']

class HistoricoTreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoTreino
        fields = '__all__'

class HistoricoDietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoDieta
        fields = '__all__'

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = '__all__'

class RefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refeicao
        fields = '__all__'

class TrocaExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrocaExercicio
        fields = '__all__'

class TrocaRefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrocaRefeicao
        fields = '__all__'
