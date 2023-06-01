import ormar
from typing import Optional

from config import database, metadata
from models.turma import Turma
from models.usuario import Usuario
from models.curso import Curso

class Aluno(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
        tablename = 'alunos'

    id: int = ormar.Integer(primary_key = True)
    name: str = ormar.String(max_length = 50)
    ra: int = ormar.BigInteger()
    gender: str = ormar.String(max_length = 1)
    cpf: str = ormar.String(max_length = 11)
    payment: float = ormar.Float()
    birth: str = ormar.Date()
    phone: str = ormar.String(max_length = 11)

    classroom: Optional[Turma] = ormar.ForeignKey(Turma, skip_reverse=True)
    user: Optional[Usuario] = ormar.ForeignKey(Usuario, skip_reverse=True)
    course: Optional[Curso] = ormar.ForeignKey(Curso, skip_reverse=True)