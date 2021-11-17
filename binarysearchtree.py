class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
           
        else:
            trav =self.head
            while(trav):
                if data < trav.data:
                    if trav.left == None:
                        trav.left = node
                        trav = trav.left
                    
                    trav = trav.left
                else:
                    if trav.right == None:
                        trav.right = node
                        trav  = trav.right

                    trav = trav.right
                
            
t = Tree()

t.insert(20)
t.insert(15)
t.insert(11)


