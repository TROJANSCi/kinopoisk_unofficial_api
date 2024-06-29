from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class CountryItem(BaseModel):
    country: str


class Company(BaseModel):
    name: str


class Item(BaseModel):
    type: str
    sub_type: Optional[str] = Field(..., alias='subType')
    date: str
    re_release: bool = Field(..., alias='reRelease')
    country: Optional[CountryItem]
    companies: List[Company]


class Distributions(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
