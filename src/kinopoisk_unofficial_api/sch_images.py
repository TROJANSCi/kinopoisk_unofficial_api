from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    image_url: Optional[str] = Field(..., alias='imageUrl')
    preview_url: Optional[str] = Field(..., alias='previewUrl')


class Images(BaseModel):
    total: Optional[int] = None
    total_pages: Optional[int] = Field(None, alias='totalPages')
    items: Optional[List[Item]] = None
