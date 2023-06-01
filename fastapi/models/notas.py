import ormar
from typing import Optional

from config import database, metadata
from models.aluno import Aluno
from models.materia import Materia

class Notas(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
        tablename = 'notas'

    id: int = ormar.Integer(primary_key = True)
    av01: float = ormar.Float()
    av02: float = ormar.Float()
    av03: float = ormar.Float()
    average: float = ormar.Float()
    status: str = ormar.String(max_length = 1)

    studant: Optional[Aluno] = ormar.ForeignKey(Aluno)
    matter: Optional[Materia] = ormar.ForeignKey(Materia)
