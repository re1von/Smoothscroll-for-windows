from time import perf_counter
from typing import Callable


class TimerTask:
    def __init__(self, callback: Callable, timeout: int | float):
        self.callback = callback
        self.timeout = timeout
        self.start = perf_counter()
