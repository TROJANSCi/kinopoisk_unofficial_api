from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Country(BaseModel):
    country: str


class Genre(BaseModel):
    genre: str


class Information(BaseModel):
    kinopoisk_id: Optional[int] = Field(None, alias='kinopoiskId')
    kinopoisk_hd_id: Optional[str] = Field(None, alias='kinopoiskHDId')
    imdb_id: Optional[str] = Field(None, alias='imdbId')
    name_ru: Optional[str] = Field(None, alias='nameRu')
    name_en: Optional[Any] = Field(None, alias='nameEn')
    name_original: Optional[str] = Field(None, alias='nameOriginal')
    poster_url: Optional[str] = Field(None, alias='posterUrl')
    poster_url_preview: Optional[str] = Field(None, alias='posterUrlPreview')
    cover_url: Optional[str] = Field(None, alias='coverUrl')
    logo_url: Optional[str] = Field(None, alias='logoUrl')
    reviews_count: Optional[int] = Field(None, alias='reviewsCount')
    rating_good_review: Optional[float] = Field(None, alias='ratingGoodReview')
    rating_good_review_vote_count: Optional[int] = Field(
        None, alias='ratingGoodReviewVoteCount'
    )
    rating_kinopoisk: Optional[float] = Field(None, alias='ratingKinopoisk')
    rating_kinopoisk_vote_count: Optional[int] = Field(
        None, alias='ratingKinopoiskVoteCount'
    )
    rating_imdb: Optional[float] = Field(None, alias='ratingImdb')
    rating_imdb_vote_count: Optional[int] = Field(None, alias='ratingImdbVoteCount')
    rating_film_critics: Optional[Any] = Field(None, alias='ratingFilmCritics')
    rating_film_critics_vote_count: Optional[int] = Field(
        None, alias='ratingFilmCriticsVoteCount'
    )
    rating_await: Optional[float] = Field(None, alias='ratingAwait')
    rating_await_count: Optional[int] = Field(None, alias='ratingAwaitCount')
    rating_rf_critics: Optional[float] = Field(None, alias='ratingRfCritics')
    rating_rf_critics_vote_count: Optional[int] = Field(
        None, alias='ratingRfCriticsVoteCount'
    )
    web_url: Optional[str] = Field(None, alias='webUrl')
    year: Optional[int] = None
    film_length: Optional[int] = Field(None, alias='filmLength')
    slogan: Optional[str] = None
    description: Optional[str] = None
    short_description: Optional[str] = Field(None, alias='shortDescription')
    editor_annotation: Optional[Any] = Field(None, alias='editorAnnotation')
    is_tickets_available: Optional[bool] = Field(None, alias='isTicketsAvailable')
    production_status: Optional[Any] = Field(None, alias='productionStatus')
    type: Optional[str] = None
    rating_mpaa: Optional[Any] = Field(None, alias='ratingMpaa')
    rating_age_limits: Optional[str] = Field(None, alias='ratingAgeLimits')
    countries: Optional[List[Country]] = None
    genres: Optional[List[Genre]] = None
    start_year: Optional[int] = Field(None, alias='startYear')
    end_year: Optional[Any] = Field(None, alias='endYear')
    serial: Optional[bool] = None
    short_film: Optional[bool] = Field(None, alias='shortFilm')
    completed: Optional[bool] = None
    has_imax: Optional[bool] = Field(None, alias='hasImax')
    has3_d: Optional[bool] = Field(None, alias='has3D')
    last_sync: Optional[str] = Field(None, alias='lastSync')
