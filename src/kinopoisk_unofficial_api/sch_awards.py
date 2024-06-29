from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Person(BaseModel):
    kinopoisk_id: int = Field(..., alias='kinopoiskId')
    web_url: str = Field(..., alias='webUrl')
    name_ru: str = Field(..., alias='nameRu')
    name_en: str = Field(..., alias='nameEn')
    sex: str
    poster_url: str = Field(..., alias='posterUrl')
    growth: Optional[int]
    birthday: Optional[str]
    death: Any
    age: Optional[int]
    birthplace: Optional[str]
    deathplace: Any
    profession: Optional[str]


class Item(BaseModel):
    name: str
    win: bool
    image_url: Optional[str] = Field(..., alias='imageUrl')
    nomination_name: str = Field(..., alias='nominationName')
    year: int
    persons: List[Person]


class Awards(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
