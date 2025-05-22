def test_add_temperature(weather):
    weather.add_temperature('Monday', 20)
    assert weather.temperatures['Monday'] == 20


def test_get_average(weather):
    weather.add_temperature('Mon', 10)
    weather.add_temperature('Tue', 20)
    weather.add_temperature('Wed', 30)
    assert weather.get_average() == 20.0


def test_get_average_empty(weather):
    assert weather.get_average() == 0


def test_get_max_day(weather):
    weather.add_temperature('Mon', 18)
    weather.add_temperature('Tue', 25)
    weather.add_temperature('Wed', 22)
    assert weather.get_max_day() == 'Tue'


def test_get_max_day_empty(weather):
    assert weather.get_max_day() is None
