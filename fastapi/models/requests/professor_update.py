from pydantic import BaseModel
from typing import Optional

from models.usuario import Usuario

class ProfessorUpdate(BaseModel):
    name: Optional[str] = None
    cpf: Optional[str] = None
    salario: Optional[float] = None
    start_date: Optional[str] = None
    birth: Optional[str] = None
    user: Optional[Usuario] = None
