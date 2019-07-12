from collections import defaultdict
import threading
import queue
class Foo:
    def __init__(self):
        self.q = queue.Queue()
        self.d = defaultdict(lambda : 0)
        self.lock = threading.Lock()
        self.now = 1
        self.mapping = {1: self._first, 2:self._second, 3:self._third}



    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.mapping[1] = printFirst
        with self.lock:
            self.d[1] += 1
        self.run()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.mapping[2] = printSecond
        with self.lock:
            self.d[2] += 1
        self.run()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.mapping[3] = printThird
        with self.lock:
            self.d[3] += 1
        self.run()

    def run(self):
        with self.lock:
            while True:
                if self.d[self.now] > 0:
                    self.mapping[self.now]()
                    self.d[self.now] -= 1
                    self.now += 1
                    if self.now > 3:
                        self.now = 1
                else:
                    break
                

    def _first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()


    def _second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()


    def _third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
