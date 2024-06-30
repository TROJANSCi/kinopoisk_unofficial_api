from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    type: Optional[str]
    amount: int
    currency_code: Optional[str] = Field(..., alias='currencyCode')
    name: Optional[str]
    symbol: Optional[str]


class BoxOffice(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
