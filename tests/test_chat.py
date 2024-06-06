import re
from atlas_talk.config import Config
from atlas_talk.chat import invoke, setup

def test_rag():
    config = Config('test')
    engine = setup(config)
    got = invoke(engine, "How do I create a cluster?")
    expect = 'atlas clusters create'
    assert re.search(expect, got), 'expected: ' + expect + ' got: ' + got


def test_memory():
    config = Config('test')
    engine = setup(config)
    invoke(engine, "hi I'm John, how are you?")
    got = invoke(engine, "do you remmeber my name?")
    expect = 'John'
    assert re.search(expect, got), 'expected: ' + expect + ' got: ' + got
