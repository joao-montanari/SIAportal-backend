from typing import Optional
from pydantic import BaseModel

class LivroUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    publishing_company: Optional[str] = None