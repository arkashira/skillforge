import json
from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    id: int
    title: str
    summary: str
    tags: List[str]
    links: List[str]

@dataclass
class User:
    id: int
    tech_stack: List[str]

class SkillForge:
    def __init__(self):
        self.users = {}
        self.items = []

    def add_user(self, user_id, tech_stack):
        self.users[user_id] = User(user_id, tech_stack)

    def add_item(self, item_id, title, summary, tags, links):
        self.items.append(Item(item_id, title, summary, tags, links))

    def get_dashboard(self, user_id):
        user = self.users.get(user_id)
        if user:
            filtered_items = [item for item in self.items if any(tag in user.tech_stack for tag in item.tags)]
            return filtered_items[:10]
        return []

    def get_item_detail(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def update_tech_stack(self, user_id, new_tech_stack):
        user = self.users.get(user_id)
        if user:
            user.tech_stack = new_tech_stack

    @staticmethod
    def load_data(skill_forge, data):
        for user in data['users']:
            skill_forge.add_user(user['id'], user['tech_stack'])
        for item in data['items']:
            skill_forge.add_item(item['id'], item['title'], item['summary'], item['tags'], item['links'])

    @staticmethod
    def save_data(skill_forge):
        data = {
            'users': [{'id': user.id, 'tech_stack': user.tech_stack} for user in skill_forge.users.values()],
            'items': [{'id': item.id, 'title': item.title, 'summary': item.summary, 'tags': item.tags, 'links': item.links} for item in skill_forge.items]
        }
        return data
