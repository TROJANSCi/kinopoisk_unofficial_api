from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Film(BaseModel):
    film_id: int = Field(..., alias='filmId')
    name_ru: str = Field(..., alias='nameRu')
    name_en: Any = Field(..., alias='nameEn')
    rating: Optional[str]
    general: bool
    description: str
    profession_key: str = Field(..., alias='professionKey')


class Staff(BaseModel):
    person_id: Optional[int] = Field(None, alias='personId')
    web_url: Optional[str] = Field(None, alias='webUrl')
    name_ru: Optional[str] = Field(None, alias='nameRu')
    name_en: Optional[str] = Field(None, alias='nameEn')
    sex: Optional[str] = None
    poster_url: Optional[str] = Field(None, alias='posterUrl')
    growth: Optional[int] = None
    birthday: Optional[str] = None
    death: Optional[Any] = None
    age: Optional[int] = None
    birthplace: Optional[str] = None
    deathplace: Optional[Any] = None
    spouses: Optional[List] = None
    has_awards: Optional[int] = Field(None, alias='hasAwards')
    profession: Optional[str] = None
    facts: Optional[List] = None
    films: Optional[List[Film]] = None
