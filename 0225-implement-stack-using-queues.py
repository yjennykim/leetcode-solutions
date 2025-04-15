from queue import Queue

class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        tmp = Queue()
        while self.q.qsize() > 1:
            oldest = self.q.get()
            tmp.put(oldest)
        newest = self.q.get()
        self.q = tmp
        return newest

    def top(self) -> int:
        tmp = Queue()
        while self.q.qsize() > 1:
            oldest = self.q.get()
            tmp.put(oldest)
        newest = self.q.get()
        tmp.put(newest)
        self.q = tmp
        return newest

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()