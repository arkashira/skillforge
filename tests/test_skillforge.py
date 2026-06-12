import pytest
from skillforge import SkillForge, Item, User

def test_add_user():
    skill_forge = SkillForge()
    skill_forge.add_user(1, ['PyTorch', 'LangChain'])
    assert len(skill_forge.users) == 1

def test_add_item():
    skill_forge = SkillForge()
    skill_forge.add_item(1, 'Item 1', 'Summary 1', ['PyTorch'], ['https://example.com'])
    assert len(skill_forge.items) == 1

def test_get_dashboard():
    skill_forge = SkillForge()
    skill_forge.add_user(1, ['PyTorch', 'LangChain'])
    skill_forge.add_item(1, 'Item 1', 'Summary 1', ['PyTorch'], ['https://example.com'])
    skill_forge.add_item(2, 'Item 2', 'Summary 2', ['LangChain'], ['https://example.com'])
    dashboard = skill_forge.get_dashboard(1)
    assert len(dashboard) == 2

def test_get_item_detail():
    skill_forge = SkillForge()
    skill_forge.add_item(1, 'Item 1', 'Summary 1', ['PyTorch'], ['https://example.com'])
    item = skill_forge.get_item_detail(1)
    assert item.title == 'Item 1'

def test_update_tech_stack():
    skill_forge = SkillForge()
    skill_forge.add_user(1, ['PyTorch', 'LangChain'])
    skill_forge.update_tech_stack(1, ['TensorFlow', 'Keras'])
    user = skill_forge.users.get(1)
    assert user.tech_stack == ['TensorFlow', 'Keras']

def test_load_data():
    skill_forge = SkillForge()
    data = {
        'users': [{'id': 1, 'tech_stack': ['PyTorch', 'LangChain']}],
        'items': [{'id': 1, 'title': 'Item 1', 'summary': 'Summary 1', 'tags': ['PyTorch'], 'links': ['https://example.com']}]
    }
    SkillForge.load_data(skill_forge, data)
    assert len(skill_forge.users) == 1
    assert len(skill_forge.items) == 1

def test_save_data():
    skill_forge = SkillForge()
    skill_forge.add_user(1, ['PyTorch', 'LangChain'])
    skill_forge.add_item(1, 'Item 1', 'Summary 1', ['PyTorch'], ['https://example.com'])
    data = SkillForge.save_data(skill_forge)
    assert len(data['users']) == 1
    assert len(data['items']) == 1
