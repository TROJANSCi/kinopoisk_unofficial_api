from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Episode(BaseModel):
    season_number: Optional[int] = Field(..., alias='seasonNumber')
    episode_number: Optional[int] = Field(..., alias='episodeNumber')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    synopsis: Optional[str]
    release_date: Optional[str] = Field(..., alias='releaseDate')


class Item(BaseModel):
    number: Optional[int] = None
    episodes: List[Episode]


class Seasons(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
