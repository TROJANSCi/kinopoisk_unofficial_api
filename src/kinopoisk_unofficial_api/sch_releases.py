from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Release(BaseModel):
    film_id: int = Field(..., alias='filmId')
    name_ru: str = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    year: int
    poster_url: str = Field(..., alias='posterUrl')
    poster_url_preview: str = Field(..., alias='posterUrlPreview')
    countries: List[Country]
    genres: List[Genre]
    rating: float
    rating_vote_count: int = Field(..., alias='ratingVoteCount')
    expectations_rating: Optional[float] = Field(..., alias='expectationsRating')
    expectations_rating_vote_count: int = Field(
        ..., alias='expectationsRatingVoteCount'
    )
    duration: int
    release_date: str = Field(..., alias='releaseDate')


class Releases(BaseModel):
    releases: Optional[List[Release]] = None
    page: Optional[int] = None
    total: Optional[int] = None
