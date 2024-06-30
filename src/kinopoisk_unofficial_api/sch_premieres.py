from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Item(BaseModel):
    kinopoisk_id: Optional[int] = Field(..., alias='kinopoiskId')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    year: Optional[int] = None
    poster_url: Optional[str] = Field(..., alias='posterUrl')
    poster_url_preview: Optional[str] = Field(..., alias='posterUrlPreview')
    countries: Optional[List[Country]] = None
    genres: Optional[List[Genre]] = None
    duration: Optional[int] = None
    premiere_ru: Optional[str] = Field(..., alias='premiereRu')


class Premieres(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
