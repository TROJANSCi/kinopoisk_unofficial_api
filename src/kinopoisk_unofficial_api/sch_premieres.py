from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Item(BaseModel):
    kinopoisk_id: int = Field(..., alias='kinopoiskId')
    name_ru: str = Field(..., alias='nameRu')
    name_en: str = Field(..., alias='nameEn')
    year: int
    poster_url: str = Field(..., alias='posterUrl')
    poster_url_preview: str = Field(..., alias='posterUrlPreview')
    countries: List[Country]
    genres: List[Genre]
    duration: int
    premiere_ru: str = Field(..., alias='premiereRu')


class Premieres(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
