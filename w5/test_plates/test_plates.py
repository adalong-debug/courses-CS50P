import pytest
from plates import is_valid

def test_isalpha():
    assert is_valid("9hel") == False
    assert is_valid("99hel") == False
    assert is_valid("h99") == False
    assert is_valid("hell") == True

def test_len():
    assert is_valid("HELLOyouuuuu") ==False
    assert is_valid("u") ==False
    assert is_valid("uu") ==True

def test_num():
    assert is_valid("hk55r") ==False
    assert is_valid("hk9995") ==True

def test_zero():
    assert is_valid("hk005") ==False
    assert is_valid("hk900") ==True

def test_alnum():
    assert is_valid("tr55") ==True
    assert is_valid("tr--r5") ==False

