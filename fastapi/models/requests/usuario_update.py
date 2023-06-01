from typing import List, Optional
from pydantic import BaseModel

class UsuarioUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None