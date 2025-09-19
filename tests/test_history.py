from src import history

def test_add_and_load(tmp_path):
    """
    Test adding a record to history and loading it back.

    Steps:
        1. Redirect HISTORY_FILE to a temporary path (pytest fixture `tmp_path`).
        2. Add a conversion record using history.add_record().
        3. Load the history from file.
        4. Verify:
            - History contains exactly one record.
            - The 'result' field matches the expected value.
    """
    history.HISTORY_FILE = tmp_path / "history.json"
    record = history.add_record(1, "m", "cm", 100, "Length")
    data = history.load_history()
    assert len(data) == 1
    assert data[0]["result"] == 100
