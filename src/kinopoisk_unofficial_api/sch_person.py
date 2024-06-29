from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    kinopoisk_id: int = Field(..., alias='kinopoiskId')
    web_url: str = Field(..., alias='webUrl')
    name_ru: str = Field(..., alias='nameRu')
    name_en: str = Field(..., alias='nameEn')
    sex: str
    poster_url: str = Field(..., alias='posterUrl')


class Person(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
