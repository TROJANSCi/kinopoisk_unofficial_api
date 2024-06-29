from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Item(BaseModel):
    text: str
    type: str
    spoiler: bool


class Facts(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
