from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ModelItem(BaseModel):
    film_id: Optional[int] = Field(..., alias='filmId')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    name_original: Optional[str] = Field(..., alias='nameOriginal')
    poster_url: Optional[str] = Field(..., alias='posterUrl')
    poster_url_preview: Optional[str] = Field(..., alias='posterUrlPreview')
    relation_type: Optional[str] = Field(..., alias='relationType')


class SequelsAndPrequels(BaseModel):
    items: List[ModelItem]
