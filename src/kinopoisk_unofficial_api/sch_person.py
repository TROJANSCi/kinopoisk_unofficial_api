from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    kinopoisk_id: Optional[int] = Field(..., alias='kinopoiskId')
    web_url: Optional[str] = Field(..., alias='webUrl')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    sex: Optional[str]
    poster_url: Optional[str] = Field(..., alias='posterUrl')


class Person(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
