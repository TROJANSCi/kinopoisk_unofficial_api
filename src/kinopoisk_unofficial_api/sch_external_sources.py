from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    url: Optional[str] = None
    platform: Optional[str] = None
    logo_url: Optional[str] = Field(..., alias='logoUrl')


class ExternalSources(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
