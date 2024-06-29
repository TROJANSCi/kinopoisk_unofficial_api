from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Item(BaseModel):
    kinopoisk_id: int = Field(..., alias='kinopoiskId')
    imdb_id: Optional[str] = Field(..., alias='imdbId')
    name_ru: str = Field(..., alias='nameRu')
    name_en: Any = Field(..., alias='nameEn')
    name_original: str = Field(..., alias='nameOriginal')
    countries: List[Country]
    genres: List[Genre]
    rating_kinopoisk: float = Field(..., alias='ratingKinopoisk')
    rating_imdb: float = Field(..., alias='ratingImdb')
    year: int
    type: str
    poster_url: str = Field(..., alias='posterUrl')
    poster_url_preview: str = Field(..., alias='posterUrlPreview')


class Films(BaseModel):
    total: Optional[int] = None
    total_pages: Optional[int] = Field(None, alias='totalPages')
    items: Optional[List[Item]] = None
