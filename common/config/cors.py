from pydantic import BaseSettings, Field
from typing import List


class CORSSettings(BaseSettings):
    origin: List[str] = Field(default=["*"], env="ORIGIN")
    methods: List[str] = Field(default=["*"], env="METHODS")
    headers: List[str] = Field(default=["*"], env="HEADERS")
