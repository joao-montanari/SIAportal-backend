from pydantic import BaseModel
from typing import Optional

from models.aluno import Aluno
from models.materia import Materia

class NotasUpdate(BaseModel):
    av01: Optional[float] = None
    av02: Optional[float] = None
    av03: Optional[float] = None
    avarege: Optional[float] = None
    status: Optional[str] = None
    studant: Optional[Aluno] = None
    matter: Optional[Materia] = None