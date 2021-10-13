class Solution:
  def evalRPN(self, tokens):
    q = Q.Queue()
    i = 0
    while i < len(tokens):
      if tokens[i] in ("+", "*", "/", "-"):
        b = int(q.get())
        a = int(q.get())
        if tokens[i] == "+":
          c = a + b
        elif tokens[i] == "*":
          c = a * b
        elif tokens[i] == "-":
          c = a - b
        elif tokens[i] == "/":
          c = a // b
        print('putting c', c, a, b)
        q.put(c)
      else:
        q.put(tokens[i])
      i += 1
    #q.put(tokens[0])
    return q.get()

import queue as Q
sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]), 9)
print(sol.evalRPN(["4","13","5","/","+"]), 6)
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
