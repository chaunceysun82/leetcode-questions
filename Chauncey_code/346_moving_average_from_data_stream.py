from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.window = deque([], maxlen = size)
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.window) >= self.size:
            self.sum -= self.window.popleft()

        self.window.append(val)
        self.sum += val

        return self.sum / len(self.window)

