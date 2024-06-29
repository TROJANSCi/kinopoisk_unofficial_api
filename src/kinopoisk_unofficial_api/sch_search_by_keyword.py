from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Film(BaseModel):
    film_id: int = Field(..., alias='filmId')
    name_ru: str = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(None, alias='nameEn')
    type: str
    year: str
    description: Optional[str] = None
    film_length: Optional[str] = Field(None, alias='filmLength')
    countries: List[Country]
    genres: List[Genre]
    rating: str
    rating_vote_count: int = Field(..., alias='ratingVoteCount')
    poster_url: str = Field(..., alias='posterUrl')
    poster_url_preview: str = Field(..., alias='posterUrlPreview')


class SearchByKeyword(BaseModel):
    keyword: Optional[str] = None
    pages_count: Optional[int] = Field(None, alias='pagesCount')
    films: Optional[List[Film]] = None
    search_films_count_result: Optional[int] = Field(
        None, alias='searchFilmsCountResult'
    )
