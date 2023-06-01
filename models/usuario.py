import ormar
from config import database, metadata

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'usuarios'

    id: int = ormar.Integer(primary_key = True)
    email: str = ormar.String(max_length = 50)
    password: str = ormar.String(max_length = 16)