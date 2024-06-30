from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Release(BaseModel):
    film_id: Optional[int] = Field(..., alias='filmId')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    year: Optional[int]
    poster_url: Optional[str] = Field(..., alias='posterUrl')
    poster_url_preview: Optional[str] = Field(..., alias='posterUrlPreview')
    countries: Optional[List[Country]]
    genres: Optional[List[Genre]]
    rating: Optional[float]
    rating_vote_count: Optional[int] = Field(..., alias='ratingVoteCount')
    expectations_rating: Optional[float] = Field(..., alias='expectationsRating')
    expectations_rating_vote_count: Optional[int] = Field(
        ..., alias='expectationsRatingVoteCount'
    )
    duration: Optional[int]
    release_date: Optional[str] = Field(..., alias='releaseDate')


class Releases(BaseModel):
    releases: Optional[List[Release]] = None
    page: Optional[int] = None
    total: Optional[int] = None
