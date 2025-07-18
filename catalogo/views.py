from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Produto, Entrega
from .serializers import ProdutoSerializer, EntregaSerializer
from .permissions import IsAdminUser, IsEntregadorUser, IsComumUser, IsOwnerOrAdminReadOnly

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class EntregaViewSet(viewsets.ModelViewSet):
    serializer_class = EntregaSerializer
    
    def queryset(self):
        user = self.request.user
        if user.role == 'ADMIN' or user.role == 'ENTREGADOR':
            return Entrega.objects.all().order_by('-data_criacao')
        elif user.role == 'COMUM':
            return Entrega.objects.filter(cliente=user).order_by('-data_criacao')
        return Entrega.objects.none()
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsComumUser]
        elif self.action == 'mudar_status':
            permission_classes = [IsEntregadorUser | IsAdminUser] 
        elif self.action in ['update', 'partial_update', 'retrieve']:
            permission_classes = [IsOwnerOrAdminReadOnly]
        else: 
            permission_classes = [IsAuthenticated]
            if self.action == 'destroy':
                permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(cliente=self.request.user)

    @action(detail=True, methods=['post'], url_path='mudar-status')
    def mudar_status(self, request, pk=None):
        entrega = self.get_object()
        novo_status = request.data.get('status')
        if not novo_status:
            return Response(
                {'Erro': 'A chave "status" é obrigatória no corpo da requisição'},
                status=status.HTTP_400_BAD_REQUEST
            )
        status_validos = [status[0] for status in Entrega.StatusEntrega.choices]
        if novo_status not in status_validos:
            return Response(
                {'Erro': f"Status '{novo_status}' não está na lista de status válidos( '{status_validos}' )"},
                status=status.HTTP_400_BAD_REQUEST
            )
        entrega.status = novo_status
        entrega.save()
        serializer = self.get_serializer(entrega)
        return Response(serializer.data)