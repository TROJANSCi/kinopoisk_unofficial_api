from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    kinopoisk_id: int = Field(..., alias='kinopoiskId')
    image_url: str = Field(..., alias='imageUrl')
    title: str
    description: str
    url: str
    published_at: str = Field(..., alias='publishedAt')


class News(BaseModel):
    total: Optional[int] = None
    total_pages: Optional[int] = Field(None, alias='totalPages')
    items: Optional[List[Item]] = None
