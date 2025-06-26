
from rest_framework.viewsets import ModelViewSet
from .models import tipoInsumo
from .serializers import tipoInsumoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = tipoInsumo.objects.all()
    serializer_class = tipoInsumoSerializer
    
from rest_framework.viewsets import ModelViewSet
from .models import Insumo
from .serializers import InsumoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer    
    
from rest_framework.viewsets import ModelViewSet
from .models import Cultura
from .serializers import CulturaSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer
    
from rest_framework.viewsets import ModelViewSet
from .models import Propriedade
from .serializers import PropriedadeSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer

from rest_framework.viewsets import ModelViewSet
from .models import Funcionario
from .serializers import FuncionarioSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    
from rest_framework.viewsets import ModelViewSet
from .models import Tarefa
from .serializers import TarefaSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    
from rest_framework.viewsets import ModelViewSet
from .models import Colheita
from .serializers import ColheitaSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Colheita.objects.all()
    serializer_class = ColheitaSerializer
    
from rest_framework.viewsets import ModelViewSet
from .models import Plantio
from .serializers import PlantioSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Plantio.objects.all()
    serializer_class = PlantioSerializer
    
from rest_framework.viewsets import ModelViewSet
from .models import UsoInsumo
from .serializers import UsoInsumoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = UsoInsumo.objects.all()
    serializer_class = UsoInsumoSerializer                            
