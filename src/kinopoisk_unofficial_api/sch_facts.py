from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Item(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None
    spoiler: Optional[bool]


class Facts(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
