from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EstadoViewSet

router = DefaultRouter()
router.register(r'tipoInsumo', tipoInsumoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'Insumo', InsumoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'Cultura', CulturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'Propriedade', PropriedadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'Funcionario', FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'Tarefa', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'Colheita', ColheitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'Plantio', PlantioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register(r'UsoInsumo', UsoInsumoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]