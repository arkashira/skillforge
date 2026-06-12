"""Core logic for the SkillForge personalized learning feed."""

from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from typing import List, Set, Dict, Optional


@dataclass(frozen=True)
class Item:
    """Represents a learning item (article, video, etc.)."""
    id: int
    title: str
    tags: Set[str]
    summary: str
    links: List[str]
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.utcnow)

    def __post_init__(self):
        if not self.tags:
            raise ValueError("Item must have at least one tag")
        if not self.links:
            raise ValueError("Item must have at least one link")


class UserProfile:
    """Stores a user's tech‑stack preferences."""

    MAX_TAGS = 10

    def __init__(self, user_id: int, name: str, tags: Optional[Set[str]] = None):
        self.user_id = user_id
        self.name = name
        self._tags: Set[str] = set()
        if tags:
            self.set_tags(tags)

    @property
    def tags(self) -> Set[str]:
        """Return a copy of the user's tags."""
        return set(self._tags)

    def add_tag(self, tag: str) -> None:
        """Add a tag to the user's preferences."""
        if tag in self._tags:
            return
        if len(self._tags) >= self.MAX_TAGS:
            raise ValueError(f"Cannot add more than {self.MAX_TAGS} tags")
        self._tags.add(tag)

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the user's preferences."""
        self._tags.discard(tag)

    def set_tags(self, tags: Set[str]) -> None:
        """Replace the user's tags with a new set."""
        if len(tags) > self.MAX_TAGS:
            raise ValueError(f"Cannot have more than {self.MAX_TAGS} tags")
        self._tags = set(tags)


class Feed:
    """In‑memory feed of learning items."""

    def __init__(self):
        self._items: Dict[int, Item] = {}

    def add_item(self, item: Item) -> None:
        if item.id in self._items:
            raise ValueError(f"Item with id {item.id} already exists")
        self._items[item.id] = item

    def get_latest_items(self, user_tags: Set[str], limit: int = 10) -> List[Item]:
        """Return the latest items that match any of the user's tags."""
        # Filter items that have at least one matching tag
        matched = [
            item for item in self._items.values()
            if item.tags & user_tags
        ]
        # Sort by timestamp descending
        matched.sort(key=lambda i: i.timestamp, reverse=True)
        return matched[:limit]

    def get_item_detail(self, item_id: int) -> Item:
        """Return the full item detail for a given id."""
        try:
            return self._items[item_id]
        except KeyError as exc:
            raise KeyError(f"Item with id {item_id} not found") from exc

    @property
    def all_items(self) -> List[Item]:
        """Return all items in the feed."""
        return list(self._items.values())
