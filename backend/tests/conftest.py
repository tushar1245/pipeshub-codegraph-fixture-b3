import pytest

from tests.fakes import FakeDatabase


@pytest.fixture
def db():
    return FakeDatabase()
