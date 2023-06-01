import ormar
from typing import Optional

from config import database, metadata
from professor import Professor

class Turma(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
        tablename = 'turmas'

    id: int = ormar.Integer(primary_key = True)
    name: str = ormar.String(max_length = 50)
    duracao: float = ormar.Float()
    start_date: str = ormar.Date()
    
    dean: Optional[Professor] = ormar.ForeignKey(Professor)
