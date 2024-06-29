from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    film_id: int = Field(..., alias='filmId')
    name_ru: str = Field(..., alias='nameRu')
    name_en: str = Field(..., alias='nameEn')
    name_original: str = Field(..., alias='nameOriginal')
    poster_url: str = Field(..., alias='posterUrl')
    poster_url_preview: str = Field(..., alias='posterUrlPreview')
    relation_type: str = Field(..., alias='relationType')


class Similars(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
