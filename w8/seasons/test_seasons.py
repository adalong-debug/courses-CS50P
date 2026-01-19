import pytest
from seasons import convert
def test_main():
    assert convert("2025-01-12") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2024-01-12") == "One million, fifty-two thousand, six hundred forty minutes"
