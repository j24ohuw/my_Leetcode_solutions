#https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

class MyQueue(object):
    def __init__(self):
        self.values = []
    
    def peek(self):
        return self.values[0]
        
    def pop(self):
        return_val = self.values[0]
        self.values = self.values[1:]
        return return_val
    
    def put(self, value):
        self.values.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
