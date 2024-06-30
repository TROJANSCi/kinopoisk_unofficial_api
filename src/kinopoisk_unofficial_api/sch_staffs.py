from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ModelItem(BaseModel):
    staff_id: Optional[int] = Field(..., alias='staffId')
    name_ru: Optional[str] = Field(..., alias='nameRu')
    name_en: Optional[str] = Field(..., alias='nameEn')
    description: Optional[str] = None
    poster_url: Optional[str] = Field(..., alias='posterUrl')
    profession_text: Optional[str] = Field(..., alias='professionText')
    profession_key: Optional[str] = Field(..., alias='professionKey')


class Staffs(BaseModel):
    items: List[ModelItem]
