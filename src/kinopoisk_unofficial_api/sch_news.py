from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    kinopoisk_id: Optional[int] = Field(..., alias='kinopoiskId')
    image_url: Optional[str] = Field(..., alias='imageUrl')
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    published_at: Optional[str] = Field(..., alias='publishedAt')


class News(BaseModel):
    total: Optional[int] = None
    total_pages: Optional[int] = Field(None, alias='totalPages')
    items: Optional[List[Item]] = None
