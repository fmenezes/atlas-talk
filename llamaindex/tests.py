import re
from llamaindex.main import invoke, setup

def test_rag():
    engine = setup()
    got = invoke(engine, "Do you know what MongoDB Atlas is?")
    expect = 'MongoDB Atlas'
    assert re.search(expect, got), 'expected: ' + expect + ' got: ' + got


def test_memory():
    engine = setup()
    invoke(engine, "hi I'm John, how are you?")
    got = invoke(engine, "do you remmeber my name?")
    expect = 'John'
    assert re.search(expect, got), 'expected: ' + expect + ' got: ' + got


if __name__ == "__main__":
    test_rag()
    test_memory()
    print("Everything passed")
