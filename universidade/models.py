from django.db import models

class Usuario(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=16)

    def __str__(self):
        return self.email
    
class Curso(models.Model):
    PERIODOS = (
        ('I', 'Indefinido'),
        ('M', 'Manha'),
        ('T', 'Tarde'),
        ('N', 'Noite')
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

    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    contratacao = models.DateField()
    nascimento = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField()
    reitor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    SEXO = (
        ('I', 'Indefinido'),
        ('M', 'Masculino'),
        ('F', 'Feminino')
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
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    
class Materia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

class Notas(models.Model):
    STATUS = (
        ('A', 'Aprovado'),
        ('R', 'Reprovado'),
        ('C', 'Cursando'),
        ('P', 'Pendente')
    )

    av_01 = models.DecimalField(max_digits=3, decimal_places=1)
    av_02 = models.DecimalField(max_digits=3, decimal_places=1)
    av_03 = models.DecimalField(max_digits=3, decimal_places=1)
    media = models.DecimalField(max_digits=3, decimal_places=1)
    aluno_status = models.CharField(
        max_length = 1,
        choices = STATUS,
        blank = False,
        null = False,
        default = 'P'
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)


class Grade(models.Model):
    PERIODOS = (
        ('I', 'Indefinido'),
        ('M', 'Manha'),
        ('T', 'Tarde'),
        ('N', 'Noite')
    )

    periodo = models.CharField(
        max_length = 1,
        choices = PERIODOS,
        blank = False,
        null = False,
        default = 'I'
    )
    dia_semana = models.CharField(max_length=30)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)

class Livro(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editor = models.CharField(max_length=50)