### create a node class which represent the nodeof a link list
class node:
    def __init__(self, data=None):
        self.data=data
        self.nextnode=None

#### create a link list which represent a node of a linklist

class linklist:
    def __init__(self):
        self.head=node()
        ### I insert node at the end of the link list
    def append(self,data):
        new_node= node(data)
        cur= self.head
        while cur.nextnode!= None:
            cur= cur.nextnode
        cur.nextnode=new_node
        new_node=None
        ## insert node at the beginning of the link list
    def append_start(self,data):
        new_node= node(data)
        
        new_node.nextnode=self.head
        self.head=new_node
        ## insert node at the middle of the list
    def append_middle(self,data):
        new_node= node(data)
        cur= self.head
        while cur.data != 4:
            cur=cur.nextnode
        new_node.nextnode=cur.nextnode
        cur.nextnode=new_node
        cur=None
        new_node=None


    ### count no of node in link list
    def length(self):
        cur=self.head
        total=0
        while cur.nextnode!=None:
            total= total+1
            cur=cur.nextnode
        return total
    


## traverse single link list
    def display(self):
        listdata=[]
        cur_node= self.head
        while cur_node.nextnode!= None:
            cur_node=cur_node.nextnode
            listdata.append(cur_node.data)
        print (listdata)
## create object
my_list= linklist()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append(8)
my_list.append(9)
my_list.append(10)
my_list.append_middle(11)
my_list.append_middle(12)
my_list.append_middle(13)
my_list.append_start('a')


my_list.display()
print(my_list.length())

