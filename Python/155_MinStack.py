class MinStack:

    def __init__(self):
        self.l = []

    def push(self, val: int) -> None:
      if self.l == []:
        self.l.append((val, val))
      else:
        self.l.append((val, min(val, self.l[-1][1])))

    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        return self.l[-1][0]

    def getMin(self) -> int:
        return self.l[-1][1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print('c0')
obj.push(123)
print('c1')
print(obj.l)
print(obj.pop())
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.getMin())
