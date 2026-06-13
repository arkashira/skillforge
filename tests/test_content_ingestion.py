import pytest
from src.content_ingestion import ContentIngestionEngine, Item

def test_fetch_items():
    engine = ContentIngestionEngine(["source1", "source2"], [])
    items = engine.fetch_items()
    assert len(items) == 2
    assert isinstance(items[0], Item)

def test_store_items():
    db = []
    engine = ContentIngestionEngine(["source1"], db)
    items = [Item("title1", "source1", "2022-01-01", 0.8)]
    engine.store_items(items)
    assert len(db) == 1
    assert db[0] == items[0]

def test_flag_relevant_items():
    engine = ContentIngestionEngine(["source1"], [])
    items = [Item("title1", "source1", "2022-01-01", 0.8), Item("title2", "source2", "2022-01-02", 0.6)]
    relevant_items = engine.flag_relevant_items(items)
    assert len(relevant_items) == 1
    assert relevant_items[0] == items[0]

def test_flag_relevant_items_edge_case():
    engine = ContentIngestionEngine(["source1"], [])
    items = [Item("title1", "source1", "2022-01-01", 0.7), Item("title2", "source1", "2022-01-02", 0.7)]
    relevant_items = engine.flag_relevant_items(items)
    assert len(relevant_items) == 2
    assert relevant_items[0] == items[0]
    assert relevant_items[1] == items[1]

def test_main():
    # Simulate running the main function
    import sys
    sys.argv = ["content_ingestion.py", "--rss-sources", "source1", "source2", "source3", "source4", "source5"]
    from src.content_ingestion import ContentIngestionEngine
    engine = ContentIngestionEngine(["source1", "source2"], [])
    engine.main()
    # Check that the main function runs without errors
    assert True
