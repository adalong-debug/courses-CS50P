import pytest
from working import convert

def test_no_min():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_pm():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_pm_am():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_err():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
