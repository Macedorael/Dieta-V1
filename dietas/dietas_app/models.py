from django.db import models

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True )

    class Meta:
        abstract = True

class Paciente(Base):
    nome = models.CharField('nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')

    def __str__(self):
        return self.nome
 

class Medida(Base):
    nome = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    peso = models.DecimalField('Peso', max_digits=15, decimal_places=2)
    altura = models.DecimalField('Altura', max_digits=15, decimal_places=2)
    imc = models.DecimalField('Imc', max_digits=15,decimal_places=3)
    classificacao = models.CharField('Classificação', max_length=20)
    
    def __str__(self) -> str:
        return f'{self.nome}'


class Alimento(Base):
    nome = models.CharField('Nome', max_length=100)
    peso = models.DecimalField('Peso', max_digits=15,decimal_places=3)
    proteina = models.DecimalField('Proteina', max_digits=15, decimal_places=3)

    def __str__(self) -> str:
        return self.nome
    
class Refeicao(Base):
    refeicoes = models.CharField('Refeições',max_length=30)

    def __str__(self) -> str:
        return f'{self.refeicoes}'
    
class Dietas(Base):
    refeicoes = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.refeicoes}'
    
