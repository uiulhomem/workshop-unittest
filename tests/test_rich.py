from unittest.mock import MagicMock
import pytest

from app.rich import Rich


@pytest.fixture
def rich():
    obj_rich = Rich()
    obj_rich.talk = MagicMock(return_value=None)

    return obj_rich

def test_daily(rich):
    output = rich.daily()

    assert output == 'Nexxxxxxxxxxxxxxtchy!'

def test_rich_love(rich):
    entry = 'Victão'

    output = rich.rich_love(entry)

    assert output == 'Fortchy!'
