import ormar
from typing import Optional

from config import database, metadata
from models.usuario import Usuario

class Professor(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
        tablename = 'professores'

    id: int = ormar.Integer(primary_key = True)
    name: str = ormar.String(max_length = 50)
    cpf: str = ormar.String(max_length = 11)
    salario: float = ormar.Float()
    start_date: str = ormar.Date()
    birth: str = ormar.Date()
    
    user: Optional[Usuario] = ormar.ForeignKey(Usuario, skip_reverse=True)
