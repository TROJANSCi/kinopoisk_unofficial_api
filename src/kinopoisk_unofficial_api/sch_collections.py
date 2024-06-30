from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Item(BaseModel):
    kinopoisk_id: Optional[int] = Field(..., alias='kinopoiskId')
    imdb_id: Optional[str] = Field(..., alias='imdbId')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    name_original: Optional[str] = Field(..., alias='nameOriginal')
    countries: Optional[List[Country]]
    genres: Optional[List[Genre]]
    rating_kinopoisk: Optional[float] = Field(..., alias='ratingKinopoisk')
    rating_imdb: Optional[float] = Field(..., alias='ratingImdb')
    year: Optional[int]
    type: Optional[str]
    poster_url: Optional[str] = Field(..., alias='posterUrl')
    poster_url_preview: Optional[str] = Field(..., alias='posterUrlPreview')
    cover_url: Optional[str] = Field(..., alias='coverUrl')
    logo_url: Optional[str] = Field(..., alias='logoUrl')
    description: Optional[str]
    rating_age_limits: Optional[str] = Field(..., alias='ratingAgeLimits')


class Collections(BaseModel):
    total: Optional[int] = None
    total_pages: Optional[int] = Field(None, alias='totalPages')
    items: Optional[List[Item]] = None
