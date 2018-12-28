class rev:
    def __init__(self):
        self.itmes=[]
        self.re=[]
    def push(self,item):
        self.itmes.append(item)
    def pop(self):
        for i in self.re:
            self.re=self.itmes.pop()
            self.re=self.itmes.pop()
            self.re=self.itmes.pop()
    def get_stack(self):
        return self.itmes
    def r(self):
        return self.re



s1= rev()
s1.push('A')
s1.push('N')
s1.push('K')
s1.push('I')
s1.push('T')
print (s1.get_stack())
s1.pop()
s1.pop()
s1.pop()
s1.pop()
print (s1.r())
    
