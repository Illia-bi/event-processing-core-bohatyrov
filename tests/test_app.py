from app import process_event


def test_process_event():
    assert process_event("login") == "Processing event: login"
