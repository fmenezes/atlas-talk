import re
from langchain.main import setup, invoke


def test_rag():
    c = setup()
    session_id = "test_rag"
    got = invoke(c, session_id, "how do I create a cluster?")
    expect = 'atlas clusters create'
    assert re.search(expect, got), 'expected: ' + expect + ' got: ' + got


def test_memory():
    c = setup()
    session_id = "test_memory"
    invoke(c, session_id, "hi I'm John, how are you?")
    got = invoke(c, session_id, "do you remmeber my name?")
    expect = 'John'
    assert re.search(expect, got), 'expected: ' + expect + ' got: ' + got


if __name__ == "__main__":
    test_rag()
    test_memory()
    print("Everything passed")
