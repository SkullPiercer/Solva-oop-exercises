# Создайте класс Timer, у которого есть метод start() и stop().
# Метод start() сохраняет текущую дату и время начала (используйте datetime.datetime.now()),
# а метод stop() — текущее время окончания и возвращает разницу в секундах.

from datetime import datetime

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        self.end_time = datetime.now()
        if self.start_time is None:
            return None
        delta = self.end_time - self.start_time
        return delta.total_seconds()
