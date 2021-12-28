from pydantic import BaseModel


class BaseORMResponse(BaseModel):
    class Config:
        orm_mode = True
