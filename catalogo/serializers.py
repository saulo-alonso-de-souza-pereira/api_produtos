from rest_framework import serializers
from .models import Produto, Entrega

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco']
    
class EntregaSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True, read_only=True)

    produtos_ids = serializers.PrimaryKeyRelatedField(
        queryset = Produto.objects.all(),
        source = 'produtos',
        many = True,
        write_only = True
    )

    class Meta: 
        model = Entrega
        fields = [
            'id', 'destinatario', 'endereco', 'codigo_rastreio', 'status', 'data_criacao', 'produtos', 'produtos_ids'
        ]
        read_only_fields = ['codigo_rastreio', 'data_criacao', 'status']