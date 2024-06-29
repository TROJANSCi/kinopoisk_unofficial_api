from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    type: str
    amount: int
    currency_code: str = Field(..., alias='currencyCode')
    name: str
    symbol: str


class BoxOffice(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
