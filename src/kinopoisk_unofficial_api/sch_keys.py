from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class TotalQuota(BaseModel):
    value: int
    used: int


class DailyQuota(BaseModel):
    value: int
    used: int


class Keys(BaseModel):
    total_quota: Optional[TotalQuota] = Field(None, alias='totalQuota')
    daily_quota: Optional[DailyQuota] = Field(None, alias='dailyQuota')
    account_type: Optional[str] = Field(None, alias='accountType')
