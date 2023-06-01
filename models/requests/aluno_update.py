from typing import Optional
from pydantic import BaseModel

from models.turma import Turma
from models.usuario import Usuario
from models.curso import Curso

class AlunoUpdate(BaseModel):
    name: Optional[str] = None
    ra: Optional[str] = None
    gender: Optional[str] = None
    cpf: Optional[str] = None
    payment: Optional[float] = None
    birth: Optional[str] = None
    phone: Optional[str] = None
    classroom: Optional[Turma] = None
    user: Optional[Usuario] = None
    course: Optional[Curso]  = None
