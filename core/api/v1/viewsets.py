from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser as DRFIsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from core.models import (Treino, Dieta, TipoPlano, Cliente, HistoricoTreino, 
                       HistoricoDieta, Exercicio, Refeicao, TrocaExercicio, TrocaRefeicao, Perfil)
from .serializers import (TreinoSerializer, DietaSerializer, TipoPlanoSerializer,
                        ClienteSerializer, HistoricoTreinoSerializer, HistoricoDietaSerializer,
                        ExercicioSerializer, RefeicaoSerializer, TrocaExercicioSerializer,
                        TrocaRefeicaoSerializer, UserSerializer, PerfilSerializer)
from .permissions import (IsAdminUser, IsNutricionistaUser, IsPersonalUser, 
                        IsClienteUser, IsOwnerOrStaff, ReadOnly)


class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.filter(deleted_at__isnull=True)
    serializer_class = TreinoSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, (IsAdminUser | IsPersonalUser)]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return Treino.objects.filter(deleted_at__isnull=True, clientes__perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'personal']:
                return Treino.objects.filter(deleted_at__isnull=True)
        return Treino.objects.none()
    
    @swagger_auto_schema(tags=['Treinos'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class DietaViewSet(viewsets.ModelViewSet):
    queryset = Dieta.objects.filter(deleted_at__isnull=True)
    serializer_class = DietaSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, (IsAdminUser | IsNutricionistaUser)]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return Dieta.objects.filter(deleted_at__isnull=True, clientes__perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'nutricionista']:
                return Dieta.objects.filter(deleted_at__isnull=True)
        return Dieta.objects.none()
    
    @swagger_auto_schema(tags=['Dietas'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TipoPlanoViewSet(viewsets.ModelViewSet):
    queryset = TipoPlano.objects.filter(deleted_at__isnull=True)
    serializer_class = TipoPlanoSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]
    
    @swagger_auto_schema(tags=['Planos'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Planos'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Planos'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Planos'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Planos'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Planos'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(deleted_at__isnull=True)
    serializer_class = ClienteSerializer
    
    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [IsAuthenticated, (IsAdminUser | IsNutricionistaUser | IsPersonalUser)]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        elif self.action in ['create', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return Cliente.objects.filter(deleted_at__isnull=True, perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'nutricionista', 'personal']:
                return Cliente.objects.filter(deleted_at__isnull=True)
        return Cliente.objects.none()
    
    @swagger_auto_schema(tags=['Clientes'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Clientes'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Clientes'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Clientes'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Clientes'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Clientes'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class HistoricoTreinoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoTreino.objects.filter(deleted_at__isnull=True)
    serializer_class = HistoricoTreinoSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, (IsAdminUser | IsPersonalUser)]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return HistoricoTreino.objects.filter(deleted_at__isnull=True, cliente__perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'personal']:
                return HistoricoTreino.objects.filter(deleted_at__isnull=True)
        return HistoricoTreino.objects.none()
    
    @swagger_auto_schema(tags=['Histórico'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class HistoricoDietaViewSet(viewsets.ModelViewSet):
    queryset = HistoricoDieta.objects.filter(deleted_at__isnull=True)
    serializer_class = HistoricoDietaSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, (IsAdminUser | IsNutricionistaUser)]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return HistoricoDieta.objects.filter(deleted_at__isnull=True, cliente__perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'nutricionista']:
                return HistoricoDieta.objects.filter(deleted_at__isnull=True)
        return HistoricoDieta.objects.none()
    
    @swagger_auto_schema(tags=['Histórico'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Histórico'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.filter(deleted_at__isnull=True)
    serializer_class = ExercicioSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, (IsAdminUser | IsPersonalUser)]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return Exercicio.objects.filter(deleted_at__isnull=True, treino__clientes__perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'personal']:
                return Exercicio.objects.filter(deleted_at__isnull=True)
        return Exercicio.objects.none()
    
    @swagger_auto_schema(tags=['Treinos'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Treinos'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.filter(deleted_at__isnull=True)
    serializer_class = RefeicaoSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, (IsAdminUser | IsNutricionistaUser)]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return Refeicao.objects.filter(deleted_at__isnull=True, dieta__clientes__perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'nutricionista']:
                return Refeicao.objects.filter(deleted_at__isnull=True)
        return Refeicao.objects.none()
    
    @swagger_auto_schema(tags=['Dietas'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Dietas'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TrocaExercicioViewSet(viewsets.ModelViewSet):
    queryset = TrocaExercicio.objects.filter(deleted_at__isnull=True)
    serializer_class = TrocaExercicioSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        elif self.action in ['create']:
            permission_classes = [IsAuthenticated, IsClienteUser]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return TrocaExercicio.objects.filter(deleted_at__isnull=True, cliente__perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'personal']:
                return TrocaExercicio.objects.filter(deleted_at__isnull=True)
        return TrocaExercicio.objects.none()
    
    @swagger_auto_schema(tags=['Trocas'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TrocaRefeicaoViewSet(viewsets.ModelViewSet):
    queryset = TrocaRefeicao.objects.filter(deleted_at__isnull=True)
    serializer_class = TrocaRefeicaoSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        elif self.action in ['create']:
            permission_classes = [IsAuthenticated, IsClienteUser]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil'):
            if user.perfil.tipo == 'cliente' and hasattr(user.perfil, 'cliente'):
                return TrocaRefeicao.objects.filter(deleted_at__isnull=True, cliente__perfil__usuario=user)
            elif user.perfil.tipo in ['admin', 'nutricionista']:
                return TrocaRefeicao.objects.filter(deleted_at__isnull=True)
        return TrocaRefeicao.objects.none()
    
    @swagger_auto_schema(tags=['Trocas'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Trocas'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        elif self.action in ['create', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or (hasattr(user, 'perfil') and user.perfil.tipo == 'admin'):
            return User.objects.filter(is_active=True)
        return User.objects.filter(id=user.id, is_active=True)
    
    @swagger_auto_schema(tags=['Usuários'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'])
    @swagger_auto_schema(tags=['Usuários'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.filter(deleted_at__isnull=True)
    serializer_class = PerfilSerializer
    
    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        elif self.action in ['create', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or (hasattr(user, 'perfil') and user.perfil.tipo == 'admin'):
            return Perfil.objects.filter(deleted_at__isnull=True)
        return Perfil.objects.filter(usuario=user, deleted_at__isnull=True)
    
    @swagger_auto_schema(tags=['Usuários'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Usuários'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
