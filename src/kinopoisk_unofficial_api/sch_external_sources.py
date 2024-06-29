from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    url: str
    platform: str
    logo_url: str = Field(..., alias='logoUrl')


class ExternalSources(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
