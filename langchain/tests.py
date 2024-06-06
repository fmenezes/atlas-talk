import re
from src.chain import chain, invoke


def test_rag():
    c = chain()
    got = invoke(c, "foo", "how do I create a cluster?")
    expect = 'atlas clusters create'
    assert re.search(expect, got), 'expected: ' + expect + ' got: ' + got


def test_memory():
    c = chain()
    invoke(c, "foo", "hi I'm John, how are you?")
    got = invoke(c, "foo", "do you remmeber my name?")
    expect = 'John'
    assert re.search(expect, got), 'expected: ' + expect + ' got: ' + got


if __name__ == "__main__":
    test_rag()
    test_memory()
    print("Everything passed")
