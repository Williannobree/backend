from django.db import models


class tipoInsumo(models.Model):
    tipo = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.tipo     

    class Meta:
        verbose_name_plural = "Tipos de Insumo"
        verbose_name = "Tipo de Insumo"
 

class Insumo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.ForeignKey(tipoInsumo, on_delete=models.PROTECT)
    unidadeMedida = models.CharField(
    max_length=10,
    choices=[
    ('ton', 'Ton'),
    ('kg', 'Kilogram'),
    ('g', 'Gram'),
    ('mg', 'Milligram')
    ])

    def __str__(self):
        return self.nome

class Cultura(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Culturas"
        verbose_name = "Cultura"

class Propriedade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)
    area_total = models.DecimalField(max_digits=10, decimal_places=2)
    dono = models.CharField(max_length=100, blank=True, null=True)
    data_aquisicao = models.DateField()
            
    def __str__(self):
        return self.nome    

    class Meta:
        verbose_name_plural = "Propriedades"
        verbose_name = "Propriedade"
        ordering = ['nome'] 


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    Propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE, related_name='funcionarios')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Funcionários"
        verbose_name = "Funcionário"
        ordering = ['nome']
                   

class Tarefa(models.Model):
    descricao = models.CharField(max_length=255)
    data_aquisicao = models.DateField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    plantio = models.ForeignKey(Propriedade, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao   
    
    class Meta:
        verbose_name_plural = "Tarefas"
        verbose_name = "Tarefa"
        ordering = ['data_aquisicao']
        
class Colheita(models.Model):
    plantio = models.ForeignKey('Tarefa', on_delete=models.CASCADE, related_name='colheitas')
    data_colheita = models.DateField()
    quantidade_colhida = models.DecimalField(max_digits=10, decimal_places=2)
    qualidade = models.CharField(max_length=50, blank=True, null=True)   
                
    def __str__(self):
        return f"Colheita de {self.plantio} em {self.data_colheita}"
                
    class Meta:
        verbose_name_plural = "Colheitas"
        verbose_name = "Colheita"
        ordering = ['data_colheita']

class Plantio(models.Model):
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)
    data_plantio = models.DateField()
    area_plantada = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
    max_length=20,
    choices=[
        ('planejado', 'Planejado'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído')
        ],
        default='planejado'
    )

    def __str__(self):
        return f"{self.cultura} em {self.propriedade} - {self.status}"
    class Meta:
        verbose_name_plural = "Plantios"
        verbose_name = "Plantio"
        ordering = ['data_plantio']

class UsoInsumo(models.Model):    
    plantio = models.ForeignKey(Plantio, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data_uso = models.DateField()

    def __str__(self):
        return f"{self.quantidade} de {self.insumo} usado em {self.plantio}"
                                
    class Meta:
        verbose_name_plural = "Uso de Insumos"
        verbose_name = "Uso de Insumo"
        ordering = ['data_uso']
