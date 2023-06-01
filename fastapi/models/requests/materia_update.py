from pydantic import BaseModel
from typing import Optional

from models.curso import Curso
from models.professor import Professor

class MateriaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    hours: Optional[float] = None
    course: Optional[Curso] = None
    professor: Optional[Professor] = None
