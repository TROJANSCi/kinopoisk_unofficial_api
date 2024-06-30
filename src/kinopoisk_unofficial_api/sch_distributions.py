from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class CountryItem(BaseModel):
    country: str


class Company(BaseModel):
    name: str


class Item(BaseModel):
    type: Optional[str] = None
    sub_type: Optional[str] = Field(..., alias='subType')
    date: Optional[str] = None
    re_release: Optional[bool] = Field(..., alias='reRelease')
    country: Optional[CountryItem] = None
    companies: Optional[List[Company]] = None


class Distributions(BaseModel):
    total: Optional[int] = None
    items: Optional[List[Item]] = None
