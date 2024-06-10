from pydantic import BaseModel

class ItemCreateSchema(BaseModel):
    name: str
    description: str