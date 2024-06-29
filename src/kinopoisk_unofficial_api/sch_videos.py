from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Item(BaseModel):
    url: str
    name: str
    site: str


class Videos(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
