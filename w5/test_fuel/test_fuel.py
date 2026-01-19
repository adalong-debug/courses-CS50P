import pytest
from fuel import convert,gauge

def test_convert():
    assert convert("1/5") == 20

def test_gauge():
    assert gauge(99) =="F"
    assert gauge(1) =="E"
    assert gauge(59) =="59%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_int():
    with pytest.raises(ValueError):
        convert("9.5/10")
        convert("9/10.5")
        convert("11/10")
        convert("-11/10")
