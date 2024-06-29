from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ModelItem(BaseModel):
    staff_id: int = Field(..., alias='staffId')
    name_ru: str = Field(..., alias='nameRu')
    name_en: str = Field(..., alias='nameEn')
    description: Optional[str]
    poster_url: str = Field(..., alias='posterUrl')
    profession_text: str = Field(..., alias='professionText')
    profession_key: str = Field(..., alias='professionKey')


class Staffs(BaseModel):
    items: List[ModelItem]
