import pytest
from numb3rs import validate

def test_normal():
    assert validate("255.0.0.1") == True

def test_edge():
    assert validate("512.512.512.512") == False

def test_part():
    assert validate("1.2.3.1000") == False

def test_zero():
    assert validate("192.168.001.1") == False

def test_cat():
    assert validate("cat") == False
