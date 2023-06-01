import ormar
from typing import Optional

from config import database, metadata

class Livro(ormar.Model):
    class Meta:
        database = database
        metadata = metadata
        tablename = 'livros'

    id: int = ormar.Integer(primary_key = True)
    name: str = ormar.String(max_length = 50)
    category: str = ormar.String(max_length = 100)
    description: str = ormar.String(max_length = 200)
    author: str = ormar.String(max_length = 50)
    publishing_company: str = ormar.String(max_length = 50)