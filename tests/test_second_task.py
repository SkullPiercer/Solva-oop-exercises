from time import sleep

from tasks.second_task import Timer


def test_timer_basic_usage(create_timer):
    create_timer.start()
    sleep(1.5)
    duration = create_timer.stop()

    assert 1.4 <= duration <= 1.6, 'Длительность должна быть около 1.5 секунд'


def test_timer_without_start(create_timer):
    duration = create_timer.stop()
    assert duration is None, (
        'Если не вызывать start(), stop() должен вернуть None'
    )


def test_timer_multiple_calls(create_timer):
    create_timer.start()
    sleep(0.5)
    d1 = create_timer.stop()

    create_timer.start()
    sleep(0.7)
    d2 = create_timer.stop()

    assert 0.4 <= d1 <= 0.6, (
        'Первая сессия: длительность должна быть около 0.5 секунд'
    )
    assert 0.6 <= d2 <= 0.8, (
        'Вторая сессия: длительность должна быть около 0.7 секунд'
    )
