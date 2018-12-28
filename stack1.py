
class Stack:
    def __init__(self):
        self.items=items

    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
		return self.items

s1=Stack()
s1.push("A")
s1.push("B")
print(s1.get_stack())
s1.pop()
print(s1.get_stack())
        
