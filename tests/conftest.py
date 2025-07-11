import pytest

from tasks import Timer, ToDoList, User, WeatherLog

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


@pytest.fixture()
def create_timer():
    return Timer()


@pytest.fixture
def todo():
    return ToDoList()


@pytest.fixture
def weather():
    return WeatherLog()
