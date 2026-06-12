"""Pytest suite for the SkillForge learning feed."""

import datetime
import pytest

from learning import UserProfile, Feed, Item


@pytest.fixture
def user() -> UserProfile:
    return UserProfile(user_id=1, name="Alice", tags={"Python", "PyTorch"})


@pytest.fixture
def feed() -> Feed:
    f = Feed()
    now = datetime.datetime.utcnow()
    # Create 15 items with varying tags
    for i in range(15):
        tags = {"Python"} if i % 2 == 0 else {"JavaScript"}
        tags.add("AI" if i % 3 == 0 else "Web")
        f.add_item(
            Item(
                id=i,
                title=f"Item {i}",
                tags=tags,
                summary=f"Summary of item {i}",
                links=[f"https://example.com/item{i}"],
                timestamp=now - datetime.timedelta(minutes=i),
            )
        )
    return f


def test_user_profile_tag_limit(user: UserProfile):
    # Initially has 2 tags
    assert user.tags == {"Python", "PyTorch"}
    # Add new tags up to the limit
    for n in range(8):
        user.add_tag(f"Tag{n}")
    assert len(user.tags) == 10
    # Adding one more should raise
    with pytest.raises(ValueError):
        user.add_tag("OverflowTag")


def test_user_profile_set_tags(user: UserProfile):
    # Setting tags beyond limit raises
    with pytest.raises(ValueError):
        user.set_tags({f"Tag{i}" for i in range(11)})
    # Valid set replaces existing tags
    user.set_tags({"Go", "Rust"})
    assert user.tags == {"Go", "Rust"}


def test_feed_dashboard(user: UserProfile, feed: Feed):
    # User tags are Python and PyTorch
    dashboard = feed.get_latest_items(user.tags, limit=10)
    # All items should match at least one user tag
    for item in dashboard:
        assert item.tags & user.tags
    # Should return at most 10 items
    assert len(dashboard) <= 10
    # Items should be sorted by timestamp descending
    timestamps = [item.timestamp for item in dashboard]
    assert timestamps == sorted(timestamps, reverse=True)


def test_feed_dashboard_no_match():
    f = Feed()
    now = datetime.datetime.utcnow()
    f.add_item(
        Item(
            id=1,
            title="No match",
            tags={"Java"},
            summary="No match summary",
            links=["https://example.com/no_match"],
            timestamp=now,
        )
    )
    user = UserProfile(user_id=2, name="Bob", tags={"Python"})
    dashboard = f.get_latest_items(user.tags, limit=10)
    assert dashboard == []  # No items match the user's tags


def test_item_detail(feed: Feed):
    # Pick an existing item
    item = feed.get_item_detail(3)
    assert item.id == 3
    assert item.title == "Item 3"
    assert item.summary == "Summary of item 3"
    assert len(item.links) == 1
    assert item.links[0] == "https://example.com/item3"

    # Requesting non‑existent id raises
    with pytest.raises(KeyError):
        feed.get_item_detail(999)


def test_modify_preferences_and_dashboard(user: UserProfile, feed: Feed):
    # Initially user has Python and PyTorch
    dashboard = feed.get_latest_items(user.tags, limit=10)
    assert all(item.tags & user.tags for item in dashboard)

    # Change preferences to JavaScript only
    user.set_tags({"JavaScript"})
    dashboard_js = feed.get_latest_items(user.tags, limit=10)
    assert all("JavaScript" in item.tags for item in dashboard_js)
    # Ensure items from previous dashboard are not present
    ids_prev = {item.id for item in dashboard}
    ids_js = {item.id for item in dashboard_js}
    assert ids_prev.isdisjoint(ids_js)
