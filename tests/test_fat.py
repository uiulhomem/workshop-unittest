import pytest

from app.fatorial import fatorial


def test_fatorial_result():
    result_5 = fatorial(5)
    result_3 = fatorial(3)

    assert result_5 == 120
    assert result_3 == 6

def test_non_decimal():
    with pytest.raises(ValueError):
        fatorial(0.2)

def test_negative():
    with pytest.raises(ValueError):
        fatorial(-2)

def test_fat_zero():
    result = fatorial(0)

    assert result == 1
