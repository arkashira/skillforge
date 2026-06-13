import pytest
from skillforge import SkillForge, User, Item

def test_add_user():
    skillforge = SkillForge()
    skillforge.add_user(1, ["PyTorch", "LangChain"])
    assert skillforge.users[1].tech_stack == ["PyTorch", "LangChain"]

def test_add_item():
    skillforge = SkillForge()
    skillforge.add_item(1, "Item 1", "Summary 1", ["PyTorch"], ["https://example.com"])
    assert skillforge.items[0].title == "Item 1"

def test_get_dashboard():
    skillforge = SkillForge()
    skillforge.add_user(1, ["PyTorch", "LangChain"])
    skillforge.add_item(1, "Item 1", "Summary 1", ["PyTorch"], ["https://example.com"])
    skillforge.add_item(2, "Item 2", "Summary 2", ["LangChain"], ["https://example.com"])
    dashboard = skillforge.get_dashboard(1)
    assert len(dashboard) == 2

def test_get_item():
    skillforge = SkillForge()
    skillforge.add_item(1, "Item 1", "Summary 1", ["PyTorch"], ["https://example.com"])
    item = skillforge.get_item(1)
    assert item.title == "Item 1"

def test_update_tech_stack():
    skillforge = SkillForge()
    skillforge.add_user(1, ["PyTorch", "LangChain"])
    skillforge.update_tech_stack(1, ["TensorFlow", "Keras"])
    assert skillforge.users[1].tech_stack == ["TensorFlow", "Keras"]

def test_get_dashboard_empty():
    skillforge = SkillForge()
    dashboard = skillforge.get_dashboard(1)
    assert dashboard == []

def test_get_item_none():
    skillforge = SkillForge()
    item = skillforge.get_item(1)
    assert item is None
