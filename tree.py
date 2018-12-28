
class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class tree:
    def __init__(self):
        self.root= node()

    def printtree(self):
        print(self.data)
    def preorder(self,data):
        if self.root != None:
            print("tree does not have any node")
        else:
            print(self.data)
            preorder(self.left)
            preorder(self.right)
    


tree= node(10)

print(tree.printtree())