from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Genre(BaseModel):
    id: int
    genre: str


class Country(BaseModel):
    id: int
    country: str


class Filters(BaseModel):
    genres: Optional[List[Genre]] = None
    countries: Optional[List[Country]] = None
