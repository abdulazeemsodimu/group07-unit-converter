from src import history

def test_add_and_load(tmp_path):
    history.HISTORY_FILE = tmp_path / "history.json"
    record = history.add_record(1, "m", "cm", 100, "Length")
    data = history.load_history()
    assert len(data) == 1
    assert data[0]["result"] == 100
