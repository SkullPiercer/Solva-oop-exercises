import pytest

from tasks.first_task import User

FIRST_TASK_DATA = {
    'andrey': 18,
    'Oleg': 13,
    'Александр': 24,
    'Ксюша': 31,
    'макс': 25,
}

@pytest.fixture()
def create_users():
    return [User(name, age) for name, age in FIRST_TASK_DATA.items()]
