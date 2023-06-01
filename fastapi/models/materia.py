import ormar
from typing import Optional

from config import database, metadata
from models.curso import Curso
from models.professor import Professor

class Materia(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
        tablename = 'materias'

    id: int  = ormar.Integer(primary_key = True)
    name: str = ormar.String(max_length = 50)
    description: str = ormar.String(max_length = 200)
    hours: float = ormar.Float()

    course: Optional[Curso] = ormar.ForeignKey(Curso)
    professor: Optional[Professor] = ormar.ForeignKey(Professor)