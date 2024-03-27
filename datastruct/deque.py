# 덱 depue

from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()
    def push_front(self, data):
        self.deque.appendleft(data)
    def push_back(self, data):
        self.deque.append(data)
    def pop_front(self):
        if self.empty() == 1:
            return -1
        return self.deque.popleft()
    def pop_back(self):
        if self.empty() == 1:
            return -1
        return self.deque.pop()
    def size(self):
        return len(self.deque)
    def empty(self):
        if len(self.deque) == 0:
            return 1
        else: 
            return 0
    def front(self):
        if self.empty() == 1:
            return -1
        return self.deque[0]
    def back(self):
        if self.empty() == 1:
            return -1
        return self.deque[-1]