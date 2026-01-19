import pytest
from lines.twttr import shorten

def test_shorten():
    assert shorten("twitter") =="twttr"

def test_cap():
    assert shorten("twItter") =="twttr"

def test_num():
    assert shorten("23te45r") =="23t45r"

def test_punctuation():
    assert shorten("te,r") =="t,r"

