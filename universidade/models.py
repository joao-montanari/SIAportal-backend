from django.db import models

class Aluno(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('I', 'Indefinido')
    )

    nome = models.CharField(max_length=50)
    genero = models.CharField(
        max_length = 1,
        choices = SEXO,
        blank = False,
        null = False,
        default = 'I'
    )
    telefone = models.CharField(max_length=50)
    nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    PERIODOS = (
        ('M', 'Manha'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
        ('I', 'Indefinido')
    )

    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    periodo = models.CharField(
        max_length = 1,
        choices = PERIODOS,
        blank = False,
        null = False,
        default = 'I'
    )
    duracao = models.IntegerField()
    descricao = models.CharField(max_length=100)