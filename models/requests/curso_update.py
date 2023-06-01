from typing import Optional
from pydantic import BaseModel

class CursoUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    period: Optional[int] = None
    duration: Optional[float] = None
    description: Optional[str] = None