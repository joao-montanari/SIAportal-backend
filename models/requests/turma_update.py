from pydantic import BaseModel
from typing import Optional

from models.professor import Professor

class TurmaUpdate(BaseModel):
    name: Optional[str] = None
    duracao: Optional[float] = None
    start_date: Optional[str] = None
    dean: Optional[Professor] = None