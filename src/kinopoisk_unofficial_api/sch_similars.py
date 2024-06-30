from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    film_id: Optional[int] = Field(..., alias='filmId')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    name_original: Optional[str] = Field(..., alias='nameOriginal')
    poster_url: Optional[str] = Field(..., alias='posterUrl')
    poster_url_preview: Optional[str] = Field(..., alias='posterUrlPreview')
    relation_type: Optional[str] = Field(..., alias='relationType')


class Similars(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
