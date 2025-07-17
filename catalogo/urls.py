from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, EntregaViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'entregas', EntregaViewSet, basename='entrega')

urlpatterns = router.urls