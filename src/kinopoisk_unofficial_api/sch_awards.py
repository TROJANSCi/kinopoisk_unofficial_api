from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Person(BaseModel):
    kinopoisk_id: Optional[int] = Field(..., alias='kinopoiskId')
    web_url: Optional[str] = Field(..., alias='webUrl')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    sex: Optional[str]
    poster_url: Optional[str] = Field(..., alias='posterUrl')
    growth: Optional[int]
    birthday: Optional[str]
    death: Optional[Any]
    age: Optional[int]
    birthplace: Optional[str]
    deathplace: Optional[Any]
    profession: Optional[str]


class Item(BaseModel):
    name: Optional[str]
    win: Optional[bool]
    image_url: Optional[str] = Field(..., alias='imageUrl')
    nomination_name: Optional[str] = Field(..., alias='nominationName')
    year: Optional[int]
    persons: Optional[List[Person]]


class Awards(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
