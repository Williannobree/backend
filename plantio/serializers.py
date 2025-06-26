from rest_framework.serializers import ModelSerializer
from .models import tipoInsumo

class tipoInsumoSerializer(ModelSerializer):
    class Meta:
        model = tipoInsumo
        fields = '__all__'
        
from rest_framework.serializers import ModelSerializer
from .models import Insumo

class InsumoSerializer(ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'
        
        
from rest_framework.serializers import ModelSerializer
from .models import Cultura

class CulturaSerializer(ModelSerializer):
    class Meta:
        model = Cultura
        fields = '__all__'        
        
        
from rest_framework.serializers import ModelSerializer
from .models import Propriedade

class PropriedadeSerializer(ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'        
        
        
from rest_framework.serializers import ModelSerializer
from .models import Funcionario

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'    
        
        
from rest_framework.serializers import ModelSerializer
from .models import Tarefa

class TarefaSerializer(ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'   
        
        
from rest_framework.serializers import ModelSerializer
from .models import Colheita

class ColheitaSerializer(ModelSerializer):
    class Meta:
        model = Colheita
        fields = '__all__'       
        
        
from rest_framework.serializers import ModelSerializer
from .models import Plantio

class PlantioSerializer(ModelSerializer):
    class Meta:
        model = Plantio
        fields = '__all__'    
        
        
from rest_framework.serializers import ModelSerializer
from .models import UsoInsumo

class UsoInsumoSerializer(ModelSerializer):
    class Meta:
        model = UsoInsumo
        fields = '__all__'                      