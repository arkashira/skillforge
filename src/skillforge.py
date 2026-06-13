import json
from dataclasses import dataclass
from typing import List

@dataclass
class User:
    id: int
    tech_stack: List[str]

@dataclass
class Item:
    id: int
    title: str
    summary: str
    tags: List[str]
    links: List[str]

class SkillForge:
    def __init__(self):
        self.users = {}
        self.items = []

    def add_user(self, user_id: int, tech_stack: List[str]):
        self.users[user_id] = User(user_id, tech_stack)

    def add_item(self, item_id: int, title: str, summary: str, tags: List[str], links: List[str]):
        self.items.append(Item(item_id, title, summary, tags, links))

    def get_dashboard(self, user_id: int):
        user = self.users.get(user_id)
        if not user:
            return []
        filtered_items = [item for item in self.items if any(tag in user.tech_stack for tag in item.tags)]
        return sorted(filtered_items, key=lambda x: x.id, reverse=True)[:10]

    def get_item_detail(self, item_id: int):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def update_tech_stack(self, user_id: int, new_tech_stack: List[str]):
        user = self.users.get(user_id)
        if user:
            user.tech_stack = new_tech_stack
