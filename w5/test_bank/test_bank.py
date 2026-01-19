import pytest
from bank import value

def test_val1():
    assert value("hello") ==0

def test_cap():
    assert value("HELLO you") ==0

def test_num():
    assert value("h23te45r") ==20

def test_punctuation():
    assert value("te,r") ==100

