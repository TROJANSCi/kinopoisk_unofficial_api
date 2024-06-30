from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Film(BaseModel):
    film_id: Optional[int] = Field(None, alias='filmId')
    name_ru: Optional[str] = Field(None, alias='nameRu')
    name_en: Optional[str] = Field(None, alias='nameEn')
    type: Optional[str] = None
    year: Optional[str] = None
    description: Optional[str] = None
    film_length: Optional[str] = Field(None, alias='filmLength')
    countries: Optional[List[Country]] = None
    genres: Optional[List[Genre]] = None
    rating: Optional[str] = None
    rating_vote_count: Optional[int] = Field(None, alias='ratingVoteCount')
    poster_url: Optional[str] = Field(None, alias='posterUrl')
    poster_url_preview: Optional[str] = Field(None, alias='posterUrlPreview')


class SearchByKeyword(BaseModel):
    keyword: Optional[str] = None
    pages_count: Optional[int] = Field(None, alias='pagesCount')
    films: Optional[List[Film]] = None
    search_films_count_result: Optional[int] = Field(
        None, alias='searchFilmsCountResult'
    )
