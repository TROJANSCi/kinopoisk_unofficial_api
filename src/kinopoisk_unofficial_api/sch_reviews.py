from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    kinopoisk_id: int = Field(..., alias='kinopoiskId')
    type: str
    date: str
    positive_rating: int = Field(..., alias='positiveRating')
    negative_rating: int = Field(..., alias='negativeRating')
    author: str
    title: Optional[str]
    description: str


class Reviews(BaseModel):
    total: Optional[int] = None
    total_pages: Optional[int] = Field(None, alias='totalPages')
    total_positive_reviews: Optional[int] = Field(None, alias='totalPositiveReviews')
    total_negative_reviews: Optional[int] = Field(None, alias='totalNegativeReviews')
    total_neutral_reviews: Optional[int] = Field(None, alias='totalNeutralReviews')
    items: Optional[List[Item]] = None
