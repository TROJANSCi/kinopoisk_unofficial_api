from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Item(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None
    site: Optional[str] = None


class Videos(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
