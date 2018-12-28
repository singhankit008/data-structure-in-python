
class Stack:
    def __init__(self):
        self.items=[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)

s1=Stack()
s1.push('A')
s1.push('B')
s1.push('C')
s1.push('D')
print(s1.get_stack())
s1.pop()
s1.pop() 
s1.pop() 
s1.pop() 
s1.push('D')
print(s1.get_stack())
print(s1.is_empty())
print(s1.size())
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)
s1.push(7)
s1.push(8)
print(s1.get_stack())

