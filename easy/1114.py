"""1114. Print in Order"""

import time
from typing import Callable


class Foo:
    def __init__(self):
        self._state = 0

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._state = 1

    def second(self, printSecond: "Callable[[], None]") -> None:
        while self._state != 1:
            time.sleep(0.1)

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self._state = 2

    def third(self, printThird: "Callable[[], None]") -> None:
        while self._state != 2:
            time.sleep(0.1)

        # printThird() outputs "third". Do not change or remove this line.
        printThird()
