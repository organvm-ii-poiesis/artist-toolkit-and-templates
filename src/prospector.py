"""Grant prospecting and application helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class GrantOpportunity:
    """A grant or funding opportunity."""
    name: str
    organization: str
    deadline: date | None = None
    amount_range: str = ""
    description: str = ""
    url: str = ""
    tags: list[str] = field(default_factory=list)
    applied: bool = False

    @property
    def is_open(self) -> bool:
        if self.deadline is None:
            return True
        return date.today() <= self.deadline

    @property
    def days_until_deadline(self) -> int | None:
        if self.deadline is None:
            return None
        return (self.deadline - date.today()).days


@dataclass
class GrantTracker:
    """Track grant opportunities and applications."""
    opportunities: list[GrantOpportunity] = field(default_factory=list)

    def add(self, opportunity: GrantOpportunity) -> None:
        self.opportunities.append(opportunity)

    @property
    def open_opportunities(self) -> list[GrantOpportunity]:
        return [o for o in self.opportunities if o.is_open]

    @property
    def applied(self) -> list[GrantOpportunity]:
        return [o for o in self.opportunities if o.applied]

    def by_tag(self, tag: str) -> list[GrantOpportunity]:
        return [o for o in self.opportunities if tag in o.tags]

    def upcoming(self, days: int = 30) -> list[GrantOpportunity]:
        result = []
        for o in self.open_opportunities:
            if o.days_until_deadline is not None and o.days_until_deadline <= days:
                result.append(o)
        return sorted(result, key=lambda o: o.deadline or date.max)

    def summary(self) -> dict:
        return {
            "total": len(self.opportunities),
            "open": len(self.open_opportunities),
            "applied": len(self.applied),
        }
