import ormar
from config import database, metadata

class Curso(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'cursos'

    id: int = ormar.Integer(primary_key = True)
    name: str = ormar.String(max_length = 50)
    category: str = ormar.String(max_length = 100)
    period: int = ormar.Integer()
    duration: float = ormar.Float()
    description: str = ormar.String(max_length = 200)